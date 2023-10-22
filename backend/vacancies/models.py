from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from students.models import Student
from users.models import User


class Vacancy(models.Model):
    """Модель для хранения вакансий."""

    title = models.CharField(
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='название',
    )
    author = models.ForeignKey(
        User,
        verbose_name='автор',
        on_delete=models.CASCADE,
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
            MinValueValidator(settings.MIN_SALARY),
        ),
    )
    salary_to = models.IntegerField(
        verbose_name='зарплата до',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(settings.MIN_SALARY),
        )
    )
    city = models.CharField(
        verbose_name='город',
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
    )
    company = models.CharField(
        verbose_name='компания',
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
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

    class Meta:
        ordering = ('id',)
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'

    def __str__(self):
        return self.title


class Filter(models.Model):
    """Модель для хранения произвольных фильтров для вакансий."""

    FILTER_FIELDS_CHOICES = [
        (field.name, field.verbose_name) for field in Student._meta.fields
    ]
    vacancy = models.ForeignKey(
        Vacancy,
        related_name='filters',
        on_delete=models.CASCADE,
        verbose_name='вакансия',
    )
    field_name = models.CharField(
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
        choices=FILTER_FIELDS_CHOICES,
        verbose_name='поле фильтра',
    )
    filter_value = models.CharField(
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='значение фильтра',
    )


class VacancyStudents(models.Model):
    """Модель для хранения оценок студентов на вакансию."""

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
        default=5,
        validators=(
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        )
    )
    notes = models.TextField(
        verbose_name='заметки HR по студенту на вакансию',
        blank=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'претендент'
        verbose_name_plural = 'претенденты'

    def __str__(self):
        return f'{self.student} - {self.vacancy}'
