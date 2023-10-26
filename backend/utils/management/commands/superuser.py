import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = (
        'Создание администратора из параметров '
        'в .env файле, по умолчанию admin/admin'
    )

    def handle(self, *args, **kwargs):
        admin_name = os.getenv('ADMIN_USERNAME', default='admin')
        admin_pass = os.getenv('ADMIN_PASSWORD', default='admin')
        admin_mail = os.getenv('ADMIN_EMAIL', default='1@1.com')
        admin_firstname = os.getenv('ADMIN_FIRSTNAME', default='Max')
        admin_lastname = os.getenv('ADMIN_LASTNAME', default='Sol')

        (User.objects.filter(username=admin_name).exists()
            or User.objects.create_superuser(
                email=admin_mail,
                username=admin_name,
                first_name=admin_firstname,
                last_name=admin_lastname,
                password=admin_pass))
