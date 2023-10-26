from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import StudentViewSet, VacancyViewSet

app_name = 'api'

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('vacancies', VacancyViewSet, basename='students')

urlpatterns = (
    path('v1/', include(router.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
)
