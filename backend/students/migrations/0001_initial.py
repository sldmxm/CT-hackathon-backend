# Generated by Django 4.1 on 2023-10-26 08:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='HardSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'навык',
                'verbose_name_plural': 'навыки',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'местонахождение',
                'verbose_name_plural': 'местонахождения',
            },
        ),
        migrations.CreateModel(
            name='OfficeFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'формат места работы',
                'verbose_name_plural': 'форматы места работы',
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'специальность',
                'verbose_name_plural': 'специальности',
            },
        ),
        migrations.CreateModel(
            name='WorkFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'формат работы',
                'verbose_name_plural': 'форматы работы',
            },
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'график работы',
                'verbose_name_plural': 'графики работы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='e-mail')),
                ('telegram_username', models.CharField(blank=True, max_length=150, null=True, validators=[utils.validators.validate_telegram_username], verbose_name='телеграм')),
                ('salary_from', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='зарплата от')),
                ('image', models.ImageField(blank=True, upload_to='students_photos/', verbose_name='фото')),
                ('portfolio_link', models.URLField(blank=True, max_length=150, null=True, verbose_name='ссылка на портфолио')),
                ('resume_link', models.URLField(blank=True, max_length=150, null=True, verbose_name='ссылка на резюме')),
                ('activity_level', models.PositiveSmallIntegerField(blank=True, default=50, help_text='От 0 до 100', null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('education', models.PositiveSmallIntegerField(choices=[(0, 'Неоконченное среднее'), (1, 'Среднее образование'), (2, 'Среднее профессиональное'), (3, 'Бакалавр'), (4, 'Магистр'), (5, 'Докторантура')], verbose_name='уровень образования')),
                ('status', models.CharField(choices=[('actively_seeking', 'Активно ищу работу'), ('additional_work', 'Ищу дополнительную работу'), ('passively_seeking', 'Пассивно ищу работу'), ('open_to_offers', 'Открыт для предложений'), ('not_seeking', 'Не ищу работу')], max_length=150, verbose_name='статус поиска работы')),
                ('work_experience', models.DecimalField(choices=[(0, 'Без опыта'), (0.4, 'Менее 6 месяцев'), (0.9, 'Менее года'), (1, 'Один год'), (2, 'Два года'), (3, 'Три года'), (4, 'Четыре года'), (5, 'Пять лет'), (5.1, 'Более пяти лет')], decimal_places=1, max_digits=2, verbose_name='опыт работы')),
                ('course_list', models.ManyToManyField(to='students.course', verbose_name='курсы')),
                ('current_location', models.ForeignKey(blank=True, max_length=150, on_delete=django.db.models.deletion.RESTRICT, related_name='students', to='students.location', verbose_name='местонахождение')),
                ('hard_skills', models.ManyToManyField(to='students.hardskill', verbose_name='навыки')),
                ('location_to_relocate', models.ManyToManyField(to='students.location', verbose_name='местонахождения для переезда')),
                ('office_format', models.ManyToManyField(related_name='students', to='students.officeformat', verbose_name='форматы места работы')),
                ('specialty', models.ManyToManyField(related_name='students', to='students.specialty', verbose_name='специальность')),
                ('work_format', models.ManyToManyField(related_name='students', to='students.workformat', verbose_name='форматы работы')),
                ('work_schedule', models.ManyToManyField(related_name='students', to='students.workschedule', verbose_name='графики работы')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ('-updated_at',),
            },
        ),
    ]
