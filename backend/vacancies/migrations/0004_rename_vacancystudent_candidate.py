# Generated by Django 4.1 on 2023-10-29 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_language_studentlanguage_student_language'),
        ('vacancies', '0003_rename_vacancystudents_vacancystudent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VacancyStudent',
            new_name='Candidate',
        ),
    ]
