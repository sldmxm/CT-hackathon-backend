from django.urls import include, path
from rest_framework.routers import DefaultRouter

from students.views import StudentViewSet


app_name = 'api'

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
]
