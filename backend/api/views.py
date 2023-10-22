from rest_framework import viewsets
from students.models import Student

from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """Представление списка всех студентов или одного."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
