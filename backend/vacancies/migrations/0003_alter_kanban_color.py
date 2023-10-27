# Generated by Django 4.1 on 2023-10-27 18:57

from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_alter_vacancy_author_alter_vacancy_work_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanban',
            name='color',
            field=models.CharField(blank=True, max_length=16, validators=[utils.validators.validate_color_format], verbose_name='цвет'),
        ),
    ]