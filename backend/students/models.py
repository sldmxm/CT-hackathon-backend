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


class HardSkill(models.Model):
    """Модель навыков, которыми обладает студент (его hard skills).

    Задействована в М2М модели StudentHardSkills.
    """

    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'


class Location(models.Model):
    class Meta:
        verbose_name = 'местонахождение'
        verbose_name_plural = 'местонахождения'


class Specialty(models.Model):
    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'


class Employment(models.Model):
    class Meta:
        verbose_name = 'вид занятости'
        verbose_name_plural = 'виды занятости'


class WorkSchedule(models.Model):
    class Meta:
        verbose_name = 'график работы'
        verbose_name_plural = 'графики работы'


class WorkFormat(models.Model):
    class Meta:
        verbose_name = 'формат работы'
        verbose_name_plural = 'форматы работы'


class OfficeFormat(models.Model):
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
    salary_to = models.IntegerField(
        verbose_name='зарплата до',
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_SALARY),
        )
    )
    image = models.ImageField(
        'фото',
        upload_to='students_photos/',
        blank=True,
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
    )
    course_list = models.ManyToManyField(
        Course,
        through='StudentCourse',
        verbose_name='курсы',
    )
    hard_skills = models.ManyToManyField(
        HardSkill,
        through='StudentHardSkill',
        verbose_name='навыки',
    )
    specialty = models.ManyToManyField(
        Specialty,
        related_name='students',
        verbose_name='специальность',
    )
    employment = models.ManyToManyField(
        Employment,
        related_name='students',
        verbose_name='виды занятости',
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
    work_experience = models.DecimalField(
        'опыт работы',
        max_digits=2,
        decimal_places=1,
        choices=EXPERIENCE_CHOICES,
    )

    class Meta:
        ordering = ('-updated_at',)
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        """Возвращает полное имя студента."""
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        """Переопределённый метод.

        Сжимает изображение пользователя с сохранением пропорций.
        """
        super(Student, self).save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path)


class StudentCourse(models.Model):
    """Модель для связи студентов и курсов."""

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='студент курса'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name='пройденные курсы'
    )

    class Meta:
        verbose_name = 'курс студента'
        verbose_name_plural = 'курсы студента'
        constraints = (
            models.UniqueConstraint(
                fields=('student', 'course'),
                name='unique_student_course'
            ),
        )

    def __str__(self):
        """Возвращает имя студента и пройденный им курс."""
        return f'{self.student} прошёл курс {self.course.name}'


class StudentHardSkill(models.Model):
    """Модель для связи студентов и навыков."""

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='skills',
        verbose_name='студент'
    )
    hard_skill = models.ForeignKey(
        HardSkill,
        on_delete=models.PROTECT,
        related_name='students',
        verbose_name='навык студента'
    )

    class Meta:
        verbose_name = 'навык студента'
        verbose_name_plural = 'навыки студента'
        constraints = (
            models.UniqueConstraint(
                fields=('student', 'hard_skill'),
                name='unique_student_hard_skill'
            ),
        )

    def __str__(self):
        """Возвращает имя студента и его навык."""
        return f'{self.student} может в {self.hard_skill.name}'
