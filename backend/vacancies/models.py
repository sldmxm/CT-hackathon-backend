from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from students.models import (
    Course,
    HardSkill,
    Location,
    OfficeFormat,
    Specialty,
    Student,
    WorkFormat,
    WorkSchedule,
)
from users.models import User
from utils.image_utils import resize_image
from utils.validators import validate_color_format

import backend.constants as constants


class Grade(models.Model):
    name = models.CharField(
        'название',
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'грейд'
        verbose_name_plural = 'грейды'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Модель для хранения вакансий."""

    title = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='название',
        blank=False,
    )
    author = models.ForeignKey(
        User,
        verbose_name='автор',
        on_delete=models.CASCADE,
        related_name='vacancies',
        blank=False,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    salary_from = models.IntegerField(
        verbose_name='зарплата от',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(constants.MIN_SALARY),
        ),
    )
    salary_to = models.IntegerField(
        verbose_name='зарплата до',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(constants.MIN_SALARY),
        )
    )
    location = models.ManyToManyField(
        Location,
        verbose_name='местонахождения',
        blank=True,
    )
    company = models.CharField(
        verbose_name='компания',
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='активная',
        default=True,
    )
    is_published = models.BooleanField(
        verbose_name='публичная',
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True,
    )
    image = models.ImageField(
        'изображение',
        upload_to='vacancies_images/',
        blank=True,
    )

    grade = models.ManyToManyField(
        Grade,
        verbose_name='грейды',
        blank=True,
        related_name='vacancies',
    )
    specialty = models.ForeignKey(
        Specialty,
        verbose_name='специальность',
        on_delete=models.RESTRICT,
        related_name='vacancies',
        blank=False,
    )
    office_format = models.ForeignKey(
        OfficeFormat,
        on_delete=models.RESTRICT,
        verbose_name='формат места работы',
        bank=True,
    )
    hard_skill = models.ManyToManyField(
        HardSkill,
        verbose_name='навыки',
        blank=True,
        related_name='vacancies',
    )
    work_schedule = models.ManyToManyField(
        WorkSchedule,
        verbose_name='графики работы',
        blank=True,
        related_name='vacancies',
    )
    work_format = models.ManyToManyField(
        WorkFormat,
        verbose_name='формат работы',
        blank=True,
        related_name='vacancies',
    )
    course_list = models.ManyToManyField(
        Course,
        verbose_name='курсы',
        blank=True,
    )
    work_experience = models.PositiveSmallIntegerField(
        'опыт работы',
        choices=constants.EXPERIENCE_CHOICES,
        blank=True,
    )
    education = models.PositiveSmallIntegerField(
        'уровень образования',
        choices=constants.EDUCATION_LEVEL_CHOICES,
        blank=True,
    )

    class Meta:
        ordering = ('is_active', '-updated_at',)
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self):
        return self.title

    @property
    def display_work_experience(self):
        return dict(constants.EXPERIENCE_CHOICES).get(
            self.work_experience, None)

    @property
    def display_education(self):
        return constants.EDUCATION_LEVEL_CHOICES[self.education][1]

    def save(self, *args, **kwargs):
        """Сжимает изображение пользователя с сохранением пропорций."""
        super(Vacancy, self).save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path)


class Filter(models.Model):
    """Модель для хранения произвольных фильтров для вакансий."""

    vacancy = models.ForeignKey(
        Vacancy,
        related_name='filters',
        on_delete=models.CASCADE,
        verbose_name='вакансия',
    )
    field_name = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        choices=constants.FILTER_FIELDS_FOR_VACANCY_CHOICES,
        verbose_name='поле фильтра',
    )
    filter_value = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='значение фильтра',
    )


class Kanban(models.Model):
    name = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='название',
        blank=False,
        unique=True,
    )
    order_number = models.PositiveSmallIntegerField(
        verbose_name='номер по порядку',
        unique=True,
        null=False,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )
    color = models.CharField(
        'цвет',
        max_length=16,
        validators=[validate_color_format],
        blank=True,
    )

    class Meta:
        ordering = ('order_number',)
        verbose_name = 'канбан этап'
        verbose_name_plural = 'этапы канбана'


class VacancyStudents(models.Model):
    """Модель для хранения информации о претендентах на вакансии."""

    student = models.ForeignKey(
        Student,
        verbose_name='студент',
        on_delete=models.CASCADE,
        null=False,
        related_name='vacancies',
    )
    vacancy = models.ForeignKey(
        Vacancy,
        verbose_name='вакансия',
        on_delete=models.CASCADE,
        null=False,
        related_name='students',
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='оценка студента на вакансию',
        validators=(
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        ),
        null=True,
    )
    notes = models.TextField(
        verbose_name='заметки HR по студенту на вакансию',
        blank=True,
    )
    kanban_position = models.ForeignKey(
        Kanban,
        on_delete=models.RESTRICT,
        related_name='students',
        verbose_name='позиция в канбане',
        default=0,
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'претендент на вакансию'
        verbose_name_plural = 'претенденты на вакансии'

    def __str__(self):
        return f'{self.student} - {self.vacancy}'
