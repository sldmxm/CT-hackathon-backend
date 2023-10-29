# Generated by Django 4.1 on 2023-10-29 18:40

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
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'язык',
                'verbose_name_plural': 'языки',
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
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='фамилия')),
                ('email', models.EmailField(blank=True, max_length=150, verbose_name='e-mail')),
                ('telegram_username', models.CharField(blank=True, max_length=150, validators=[utils.validators.validate_telegram_username], verbose_name='телеграм')),
                ('salary_from', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='зарплата от')),
                ('image', models.ImageField(blank=True, upload_to='students_photos/', verbose_name='фото')),
                ('portfolio_link', models.URLField(blank=True, max_length=150, null=True, verbose_name='ссылка на портфолио')),
                ('resume_link', models.URLField(blank=True, max_length=150, null=True, verbose_name='ссылка на резюме')),
                ('activity_level', models.PositiveSmallIntegerField(blank=True, default=50, help_text='От 0 до 100', null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('education', models.PositiveSmallIntegerField(choices=[(0, 'Неоконченное среднее'), (1, 'Среднее образование'), (2, 'Среднее профессиональное'), (3, 'Бакалавр'), (4, 'Магистр'), (5, 'Докторантура')], verbose_name='уровень образования')),
                ('status', models.CharField(choices=[('actively_seeking', 'Активно ищу работу'), ('additional_work', 'Ищу дополнительную работу'), ('passively_seeking', 'Пассивно ищу работу'), ('open_to_offers', 'Открыт для предложений'), ('not_seeking', 'Не ищу работу')], max_length=150, verbose_name='статус поиска работы')),
                ('work_experience', models.PositiveSmallIntegerField(choices=[(0, 'Без опыта'), (5, 'Менее 6 месяцев'), (9, 'Менее года'), (10, 'Один год'), (20, 'Два года'), (30, 'Три года'), (40, 'Четыре года'), (50, 'Пять лет'), (51, 'Более пяти лет')], verbose_name='опыт работы')),
                ('course_list', models.ManyToManyField(blank=True, to='students.course', verbose_name='курсы')),
                ('current_location', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.RESTRICT, related_name='students', to='students.location', verbose_name='местонахождение')),
                ('hard_skills', models.ManyToManyField(to='students.hardskill', verbose_name='навыки')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ('-updated_at',),
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
            name='StudentLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=150, verbose_name='уровень')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='students.language', verbose_name='язык')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='students.student', verbose_name='студент')),
            ],
            options={
                'verbose_name': 'уровень языка',
                'verbose_name_plural': 'уровни языков',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='language',
            field=models.ManyToManyField(blank=True, through='students.StudentLanguage', to='students.language', verbose_name='языки'),
        ),
        migrations.AddField(
            model_name='student',
            name='location_to_relocate',
            field=models.ManyToManyField(blank=True, to='students.location', verbose_name='местонахождения для переезда'),
        ),
        migrations.AddField(
            model_name='student',
            name='office_format',
            field=models.ManyToManyField(related_name='students', to='students.officeformat', verbose_name='форматы места работы'),
        ),
        migrations.AddField(
            model_name='student',
            name='specialty',
            field=models.ManyToManyField(related_name='students', to='students.specialty', verbose_name='специальность'),
        ),
        migrations.AddField(
            model_name='student',
            name='work_format',
            field=models.ManyToManyField(related_name='students', to='students.workformat', verbose_name='форматы работы'),
        ),
        migrations.AddField(
            model_name='student',
            name='work_schedule',
            field=models.ManyToManyField(related_name='students', to='students.workschedule', verbose_name='графики работы'),
        ),
    ]
