from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from utils.image_utils import resize_image
from utils.validators import validate_telegram_username

from backend.constants import (
    EDUCATION_LEVEL_CHOICES,
    EXPERIENCE_CHOICES,
    LANGUAGE_LEVEL_CHOICES,
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


class Language(ReferenceModel):
    class Meta:
        verbose_name = 'язык'
        verbose_name_plural = 'языки'


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
        blank=True,
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    telegram_username = models.CharField(
        'телеграм',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        blank=True,
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
        blank=False,
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
    )
    work_format = models.ManyToManyField(
        WorkFormat,
        related_name='students',
        verbose_name='форматы работы',
    )
    office_format = models.ManyToManyField(
        OfficeFormat,
        related_name='students',
        verbose_name='форматы места работы',
    )
    language = models.ManyToManyField(
        Language,
        verbose_name='языки',
        blank=True,
        through='StudentLanguage',
    )

    # Поля с определёнными значениями
    education = models.PositiveSmallIntegerField(
        'уровень образования',
        choices=EDUCATION_LEVEL_CHOICES,
    )
    status = models.CharField(
        'статус поиска работы',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        choices=WORK_SEEKING_STATUS_CHOICES,
    )
    work_experience = models.PositiveSmallIntegerField(
        'опыт работы',
        choices=EXPERIENCE_CHOICES,
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


class StudentLanguage(models.Model):
    """Модель для хранения информации о языках студента."""

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='languages',
        verbose_name='студент',
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='язык',
    )
    level = models.CharField(
        'уровень',
        max_length=STANDARD_MAX_CHAR_FIELD_LENGTH,
        choices=LANGUAGE_LEVEL_CHOICES,
    )

    class Meta:
        verbose_name = 'уровень языка'
        verbose_name_plural = 'уровни языков'

    def __str__(self):
        return f'{self.student} - {self.language} - {self.level}'
