from django.shortcuts import get_object_or_404
from rest_framework import permissions
from vacancies.models import Vacancy


class IsAuthor(permissions.BasePermission):
    """Проверка авторства."""

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAuthorOfVacancy(permissions.BasePermission):
    def has_permission(self, request, view):
        vacancy = get_object_or_404(Vacancy, id=view.kwargs['vacancy_id'])
        return vacancy.author == request.user
