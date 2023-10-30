from django.db.models import F, Q, Value
from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Student
from vacancies.models import Candidate, Kanban, Vacancy

from .pagination import TablePagePagination
from .permissions import IsAuthor, IsAuthorOfVacancy
from .serializers import (
    CandidateAddSerializer,
    CandidateEditSerializer,
    CandidateListSerializer,
    CandidateViewSerializer,
    StudentSerializer,
    StudentsMatchingVacancySerializer,
    VacancySerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    """Данные о всех студентах."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ('get', )
    pagination_class = TablePagePagination


class VacancyViewSet(viewsets.ModelViewSet):
    """Данные о вакансиях текущего пользователя."""

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    http_method_names = ('get', 'post')

    def get_permissions(self):
        if self.action in ('retrieve', 'add_candidates'):
            return [IsAuthor(), ]
        return [IsAuthenticated(), ]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return
        if self.action == 'retrieve':
            return Vacancy.objects.all()
        return (
            self.request.user.vacancies.
            select_related('specialty', 'office_format',).
            prefetch_related(
                'location',
                'grade',
                'work_schedule',
                'work_format',
                'course_list',
                'hard_skill',
            )
        )

    @action(
        methods=['post'],
        detail=True,
    )
    def add_candidates(self, request, pk):
        """
        Добавление кандидатов в вакансию на канбан доску.

        Формат данных:
        {"student_ids": [7,8,9]}
        """
        vacancy = get_object_or_404(Vacancy, pk=pk)

        if request.user != vacancy.author:
            return Response(
                {'detail': 'Доступ запрещен.'},
                status=status.HTTP_403_FORBIDDEN)

        serializer = CandidateAddSerializer(data=request.data)
        if serializer.is_valid():
            student_ids = serializer.validated_data['student_ids']

            candidates_to_create = [
                Candidate(
                    student_id=student_id,
                    vacancy=vacancy) for student_id in student_ids
            ]
            Candidate.objects.bulk_create(candidates_to_create)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateViewSet(mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """Данные о кандидатах по вакансии для канбан-доски."""

    queryset = Vacancy.objects.all()
    serializer_class = CandidateListSerializer
    http_method_names = ('get', 'patch')

    def get_permissions(self):
        return [IsAuthorOfVacancy(), ]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return CandidateEditSerializer
        return CandidateListSerializer

    def get_queryset(self):
        vacancy_id = self.kwargs['vacancy_id']
        if self.action == 'list':
            return Vacancy.objects.filter(id=vacancy_id)
        elif self.action == 'partial_update':
            vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
            return vacancy.candidates.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        new_kanban_position = request.data.get('kanban_position')
        if new_kanban_position:
            try:
                new_kanban_position = int(new_kanban_position)
            except ValueError:
                raise serializers.ValidationError(
                    {'kanban_position': 'Введите правильное число.'}
                )
            try:
                kanban_position = Kanban.objects.get(
                    order_number=new_kanban_position)
                instance.kanban_position = kanban_position
            except Kanban.DoesNotExist:
                raise serializers.ValidationError(
                    {'kanban_position': 'Нет такой позиции на канбан доске.'}
                )

        serializer = (
            self.get_serializer(
                instance,
                data=request.data,
                partial=True,
            )
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        response_serializer = CandidateViewSerializer(
            instance=serializer.instance,
            context={'request': request}
        )
        return Response(response_serializer.data)


class StudentMatchingViewSet(mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    """Данные о студентах, которые подходят под вакансию."""

    queryset = Student.objects.all()
    serializer_class = StudentsMatchingVacancySerializer
    http_method_names = ('get', )
    pagination_class = TablePagePagination

    def get_permissions(self):
        return [IsAuthorOfVacancy(), ]

    def get_queryset(self):
        vacancy_id = self.kwargs['vacancy_id']
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        specialty_extended = f'{vacancy.title} {vacancy.specialty.name}'

        queryset = Student.objects.annotate(
            specialty_extended=Value(specialty_extended)
        ).filter(
            # location - совпадает или готов туда переехать
            Q(current_location__in=vacancy.location.all())
            | Q(location_to_relocate__in=vacancy.location.all()),

            # ищет работу или готов к предложениям
            ~Q(status='not_seeking'),

            # еще не отобран в эту вакансию
            ~Q(
                id__in=vacancy.candidates.select_related(
                    'student'
                ).values_list('student__id', flat=True)
            ),

            # заголовок вакансии и специальность
            # содержат хотя бы одну студента
            Q(specialty_extended__icontains=F('specialty__name')),

            # совпадает хотя бы один
            office_format=vacancy.office_format,
            work_schedule__in=vacancy.work_schedule.all(),
            work_format__in=vacancy.work_format.all(),
            hard_skills__in=vacancy.hard_skill.all(),

            # опыт работы не меньше требование (проверяется по id)
            work_experience__gte=vacancy.work_experience,
        ).distinct()

        for student in queryset:
            student.relocation = (
                student.location_to_relocate.filter(
                    id__in=vacancy.location.all()).exists())
            student.relevant_hard_skills = (
                student.hard_skills.filter(
                    id__in=vacancy.hard_skill.all()))

        queryset = sorted(
            queryset,
            key=lambda student: (
                -student.work_experience,
                -student.relevant_hard_skills.count(),
            )
        )

        return queryset
