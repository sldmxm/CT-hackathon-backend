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

    admins = User.objects.filter(username=admin_name)
    if admins:
        print(f'Администратор {admin_name} уже существует')
        return admins[0]
    else:
        print(f'Создан администратор {admin_name}')
        return User.objects.create_superuser(
            email=admin_mail,
            username=admin_name,
            first_name=admin_firstname,
            last_name=admin_lastname,
            password=admin_pass
        )


class Command(BaseCommand):
    help = (
        'Создание администратора из параметров '
        'в .env файле, по умолчанию admin/admin'
    )

    def handle(self, *args, **kwargs):
        get_or_create_admin()
