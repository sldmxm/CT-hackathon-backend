import csv
import os

from django.apps import apps
from django.core.management import call_command
from django.core.management.base import BaseCommand
from utils import constants
from utils.factories import (
    StudentFactory,
    UserFactory,
    VacancyFactory,
    VacancyStudentsFactory,
)


class Command(BaseCommand):
    help = '''
    Чистит БД, добавляет данные из data, генерирует остальные
    '''

    def handle(self, *args, **options):
        def import_data_from_csv():
            models = apps.get_models()

            for filename in os.listdir(constants.DATA_DIR):
                file_path = os.path.join(constants.DATA_DIR, filename)
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
                        f"Добавлено {count} записей в модель '{model_name}'.")
                else:
                    print(
                        f"Файл '{filename}' не содержит данных для импорта.")

        call_command('flush', interactive=False)

        import_data_from_csv()

        StudentFactory.create_batch(constants.STUDENTS_COUNT)
        UserFactory.create_batch(constants.USERS_COUNT)
        VacancyFactory.create_batch(constants.VACANCIES_COUNT)
        VacancyStudentsFactory.create_batch(constants.CANDIDATES_COUNT)
