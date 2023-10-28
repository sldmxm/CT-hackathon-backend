from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from utils.image_utils import resize_image
from utils.validators import validate_telegram_username

from backend.constants import (
    EDUCATION_LEVEL_CHOICES,
    EXPERIENCE_CHOICES,
    MIN_SALARY,
    STANDARD_MAX_CHAR_FIELD_LENGTH,
    WORK_SEEKING_STATUS_CHOICES,
)


class ReferenceModel(models.Model):
    name = models.CharField(
        'название',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True,
        ordering = ('id',)

    def __str__(self):
        return self.name


class Course(ReferenceModel):
    """Модель курсов, которые прошел студент.

    Задействована в М2М модели StudentCourse.
    """

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class HardSkill(ReferenceModel):
    """Модель навыков, которыми обладает студент (его hard skills).

    Задействована в М2М модели StudentHardSkills.
    """

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'


class Location(ReferenceModel):
    class Meta:
        verbose_name = 'местонахождение'
        verbose_name_plural = 'местонахождения'


class Specialty(ReferenceModel):
    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'


class WorkSchedule(ReferenceModel):
    class Meta:
        verbose_name = 'график работы'
        verbose_name_plural = 'графики работы'


class WorkFormat(ReferenceModel):
    class Meta:
        verbose_name = 'формат работы'
        verbose_name_plural = 'форматы работы'


class OfficeFormat(ReferenceModel):
    class Meta:
        verbose_name = 'формат места работы'
        verbose_name_plural = 'форматы места работы'


class Student(models.Model):
    """Модель для хранения информации о студенте."""

    first_name = models.CharField(
        'имя',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    last_name = models.CharField(
        'фамилия',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    email = models.EmailField(
        'e-mail',
        unique=True,
    )
    telegram_username = models.CharField(
        'телеграм',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
        null=True,
        validators=[validate_telegram_username],
    )
    salary_from = models.IntegerField(
        verbose_name='зарплата от',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_SALARY),
        ),
    )
    image = models.ImageField(
        'фото',
        upload_to='students_photos/',
        blank=True,
    )
    portfolio_link = models.URLField(
        'ссылка на портфолио',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    resume_link = models.URLField(
        'ссылка на резюме',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
        null=True,
    )
    activity_level = models.PositiveSmallIntegerField(
        'активность',
        help_text='От 0 до 100',
        default=50,
        validators=[MaxValueValidator(100)],
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='дата создания',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='дата изменения',
        auto_now=True,
    )
    current_location = models.ForeignKey(
        Location,
        on_delete=models.RESTRICT,
        related_name='students',
        verbose_name='местонахождение',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
    )

    #  Поля многие-ко-многим
    location_to_relocate = models.ManyToManyField(
        Location,
        verbose_name='местонахождения для переезда',
        blank=True,
    )
    course_list = models.ManyToManyField(
        Course,
        verbose_name='курсы',
        blank=True,
    )
    hard_skills = models.ManyToManyField(
        HardSkill,
        verbose_name='навыки',
        blank=True,
    )
    specialty = models.ManyToManyField(
        Specialty,
        related_name='students',
        verbose_name='специальность',
    )
    work_schedule = models.ManyToManyField(
        WorkSchedule,
        related_name='students',
        verbose_name='графики работы',
        blank=True,
    )
    work_format = models.ManyToManyField(
        WorkFormat,
        related_name='students',
        verbose_name='форматы работы',
        blank=True,
    )
    office_format = models.ManyToManyField(
        OfficeFormat,
        related_name='students',
        verbose_name='форматы места работы',
        blank=True,
    )

    # Поля с определёнными значениями
    education = models.PositiveSmallIntegerField(
        'уровень образования',
        choices=EDUCATION_LEVEL_CHOICES,
        blank=True,
    )
    status = models.CharField(
        'статус поиска работы',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        choices=WORK_SEEKING_STATUS_CHOICES,
        blank=True,
    )
    work_experience = models.PositiveSmallIntegerField(
        'опыт работы',
        choices=EXPERIENCE_CHOICES,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('-updated_at',)
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        """Возвращает полное имя студента."""
        return f'{self.first_name} {self.last_name}'

    @property
    def display_work_experience(self):
        return dict(EXPERIENCE_CHOICES).get(
            self.work_experience, None)

    @property
    def display_education(self):
        return EDUCATION_LEVEL_CHOICES[self.education][1]

    @property
    def display_status(self):
        return dict(WORK_SEEKING_STATUS_CHOICES).get(
            self.status, None)

    def save(self, *args, **kwargs):
        """Переопределённый метод.

        Сжимает изображение пользователя с сохранением пропорций.
        """
        super(Student, self).save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path)
