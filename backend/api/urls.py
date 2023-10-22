from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

app_name = 'api'

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('v1/', include(router.urls)),
]
