import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


def get_or_create_admin():
    admin_name = os.getenv('ADMIN_USERNAME', 'admin')
    admin_pass = os.getenv('ADMIN_PASSWORD', 'admin')
    admin_mail = os.getenv('ADMIN_EMAIL', '1@1.com')
    admin_firstname = os.getenv('ADMIN_FIRSTNAME', 'Max')
    admin_lastname = os.getenv('ADMIN_LASTNAME', 'Sol')

    admin, created = User.objects.get_or_create(
        username=admin_name,
        defaults={
            'password': admin_pass,
            'email': admin_mail,
            'first_name': admin_firstname,
            'last_name': admin_lastname,
        }
    )

    if created:
        admin.is_superuser = True
        admin.is_staff = True
        admin.save()
        print(f'Создан администратор {admin_name}')
    else:
        print(f'Администратор {admin_name} уже существует')

    return admin


class Command(BaseCommand):
    help = (
        'Создание администратора из параметров '
        'в .env файле, по умолчанию admin/admin'
    )

    def handle(self, *args, **kwargs):
        get_or_create_admin()
