from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CandidateViewSet, StudentViewSet, VacancyViewSet

app_name = 'api'

router = DefaultRouter()

router.register('students', StudentViewSet, basename='students')
router.register('vacancies', VacancyViewSet, basename='vacancies')
router.register(
    r'vacancies/(?P<vacancy_id>\d+)/candidates',
    CandidateViewSet,
    basename='candidates'
)
# router.register(
# r'vacancies/(?P<vacancy_id>\d+)/students', StudentSelectionViewSet)

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
