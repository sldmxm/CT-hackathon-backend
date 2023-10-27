from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from students.models import Student
from vacancies.models import Vacancy

from .serializers import StudentSerializer, VacancyViewSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Передача данных о студентах."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', ]
    permission_classes = [IsAuthenticated]


class VacancyViewSet(viewsets.ModelViewSet):
    """Передает данные о вакансиях текущего пользователя."""

    queryset = Vacancy.objects.all()
    serializer_class = VacancyViewSerializer
    http_method_names = ['get', ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return
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
