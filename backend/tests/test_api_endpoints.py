from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from .factories import StudentFactory, VacancyFactory


class MyAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = RefreshToken.for_user(self.user)
        self.api_client = self.client
        self.api_client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        self.student = StudentFactory.create(pk=1)
        self.my_vacancy = VacancyFactory.create(pk=1, author=self.user)
        self.not_my_vacancy = VacancyFactory.create(pk=2)

    def tearDown(self):
        self.student.delete()
        self.my_vacancy.delete()
        self.not_my_vacancy.delete()

    def test_student_authenticated_access(self):
        url = reverse('api:students-detail',
                      kwargs={'pk': self.student.pk})
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_unauthenticated_access(self):
        url = reverse('api:students-detail',
                      kwargs={'pk': self.student.pk})
        self.api_client.credentials(HTTP_AUTHORIZATION='')
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_my_vacancy(self):
        url = reverse('api:vacancies-detail',
                      kwargs={'pk': self.my_vacancy.pk})
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_not_my_vacancy(self):
        url = reverse('api:vacancies-detail',
                      kwargs={'pk': self.not_my_vacancy.pk})
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_candidates_to_my_vacancy(self):
        url = reverse('api:vacancies-add-candidates',
                      kwargs={'pk': self.my_vacancy.pk})
        data = {"student_ids": [1, 2, 3]}
        response = self.api_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_candidates_to_not_my_vacancy(self):
        url = reverse('api:vacancies-add-candidates',
                      kwargs={'pk': self.not_my_vacancy.pk})
        data = {"student_ids": [1, 2, 3]}
        response = self.api_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_access(self):
        url = reverse('api:vacancies-detail',
                      kwargs={'pk': self.my_vacancy.pk})
        self.api_client.credentials(HTTP_AUTHORIZATION='')
        response = self.api_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
