import csv
import os

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand
from utils.constants import (
    CANDIDATES_COUNT,
    DATA_DIR,
    STUDENTS_COUNT,
    USERS_COUNT,
    VACANCIES_COUNT,
    VACANCY_ADMIN_AUTHOR,
)
from utils.factories import (
    StudentFactory,
    UserFactory,
    VacancyFactory,
    VacancyStudentFactory,
)
from vacancies.models import Vacancy

from .superuser import Command as SuperuserCommand


class Command(BaseCommand):
    help = '''
    Чистит БД, добавляет данные из data, генерирует остальные,
    создает админа из .env, добавляет в вакансии его автором.
    '''

    def handle(self, *args, **options):
        def import_data_from_csv():
            models = apps.get_models()

            for filename in os.listdir(DATA_DIR):
                file_path = os.path.join(DATA_DIR, filename)
                model_name = os.path.splitext(filename)[0]

                model_found = False
                for model in models:
                    if model.__name__ == model_name:
                        model_found = True
                        break

                if not model_found:
                    print(f"Модель '{model_name}' не найдена в проекте.")
                    continue

                with open(file_path, 'r') as csv_file:
                    reader = csv.reader(csv_file, delimiter=';')
                    data = []
                    field_names = [
                        field.name for field in model._meta.fields[1:]]
                    for row in reader:
                        data.append(model(**dict(zip(field_names, row))))

                count = len(data)
                if count > 0:
                    model.objects.bulk_create(data)
                    print(
                        f"Добавлено {count}"
                        f" записей в модель '{model_name}'.")
                else:
                    print(
                        f"Файл '{filename}'"
                        f" не содержит данных для импорта.")

        def vacancy_author_update(new_author, vacancies_count):
            vacancies_to_update = (
                Vacancy.objects.order_by('?')[:vacancies_count])
            for vacancy in vacancies_to_update:
                vacancy.admin_author = new_author
            Vacancy.objects.bulk_update(vacancies_to_update, ['author'])

        call_command('flush', interactive=False)

        admin_user = SuperuserCommand().handle()

        import_data_from_csv()

        StudentFactory.create_batch(STUDENTS_COUNT)
        print(
            f"Добавлено {STUDENTS_COUNT}"
            f" записей в модель 'Student'.")
        UserFactory.create_batch(USERS_COUNT)
        print(
            f"Добавлено {USERS_COUNT}"
            f" записей в модель 'User'.")
        VacancyFactory.create_batch(VACANCIES_COUNT)
        print(
            f"Добавлено {VACANCIES_COUNT}"
            f" записей в модель 'Vacancy'.")
        VacancyStudentFactory.create_batch(CANDIDATES_COUNT)
        print(
            f"Добавлено {CANDIDATES_COUNT} "
            f"записей в модель 'VacancyStudent'.")

        vacancy_author_update(admin_user, VACANCY_ADMIN_AUTHOR)
