from django.test import Client, TestCase
from django.urls import reverse


class UrlTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_swagger_url(self):
        response = self.client.get(reverse('schema-swagger-ui'))
        self.assertEqual(response.status_code, 200)

    def test_redoc_url(self):
        response = self.client.get(reverse('schema-redoc'))
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

    def test_token_obtain_url(self):
        response = self.client.post(
            reverse('api:token_obtain_pair'),
            {'username': 'your_username', 'password': 'your_password'})
        self.assertEqual(response.status_code, 401)

    def test_token_refresh_url(self):
        response = self.client.post(
            reverse('api:token_refresh'),
            {'refresh': 'your_refresh_token'})
        self.assertEqual(response.status_code, 401)
