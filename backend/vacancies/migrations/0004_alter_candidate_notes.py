# Generated by Django 4.1 on 2023-10-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_vacancy_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='заметки HR по студенту на вакансию'),
        ),
    ]
