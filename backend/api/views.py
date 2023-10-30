from django.shortcuts import get_object_or_404
from rest_framework import mixins, serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from students.models import Student
from vacancies.models import Kanban, Vacancy

from .permissions import IsAuthor, IsAuthorOfVacancy
from .serializers import (
    CandidateEditSerializer,
    CandidateListSerializer,
    CandidateViewSerializer,
    StudentSerializer,
    VacancySerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    """Передает данные о всех студентах."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ('get', )


class VacancyViewSet(viewsets.ModelViewSet):
    """Передает данные о вакансиях текущего пользователя."""

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    http_method_names = ('get', )

    def get_permissions(self):
        if self.action == 'retrieve':
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


class CandidateViewSet(mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """Передает данные о кандидатах по вакансии для канбан-доски."""

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

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        response_serializer = CandidateViewSerializer(
            instance=serializer.instance,
            context={'request': request}
        )
        return Response(response_serializer.data)
