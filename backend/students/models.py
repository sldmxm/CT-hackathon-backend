from core.enums import Limits as lim
from django.db import models
from PIL import Image


class Course(models.Model):
    """Модель курсов, которые прошел студент.

    Задействована в М2М модели StudentCourse.
    """

    title = models.CharField(
        'название курса',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    slug = models.SlugField(
        'слаг курса',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
        unique=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        """Возвращает название курса."""
        return self.title


class HardSkill(models.Model):
    """Модель навыков, которыми обладает студент (его hard skills).

    Задействована в М2М модели StudentHardSkills.
    """

    title = models.CharField(
        'навыки студента',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'

    def __str__(self):
        """Название навыка."""
        return self.title


class StudentEducationLevel(models.TextChoices):
    """Вспомогательный класс.

    Выбор уровня образования студента из ограниченного списка.
    """

    INCOMPLETE_SECONDARY = 'НЕОКОНЧЕННОЕ СРЕДНЕЕ'
    COMPLETED_SECONDARY = 'СРЕДНЕЕ'
    SECONDARY_PROFESSIONAL = 'СРЕДНЕЕ ПРОФЕССИОНАЛЬНОЕ'
    INCOMPLETE_HIGHER = 'НЕОКОНЧЕННОЕ ВЫСШЕЕ'
    COMPLETED_HIGHER = 'ВЫСШЕЕ'


class StudentStatus(models.TextChoices):
    """Вспомогательный класс.

    Для выбора статуса поиска работы студентом.
    """

    ACTIVELY_SEARCHING = 'АКТИВНО ИЩУ РАБОТУ'
    INCOMING_OFFERS = 'РАССМАТРИВАЮ ВХОДЯЩИЕ ПРЕДЛОЖЕНИЯ'
    INTERNSHIP_ONLY = 'РАССМАТРИВАЮ ТОЛЬКО СТАЖИРОВКИ'
    NOT_SEARCHING = 'НЕ ИЩУ РАБОТУ'
    EMPLOYED = 'ТРУДОУСТРОЕН'


class Student(models.Model):
    """Модель для хранения информации о студенте."""

    first_name = models.CharField(
        'имя студента',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    last_name = models.CharField(
        'фамилия студента',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    location = models.CharField(
        'местоположение',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    education = models.CharField(
        'уровень образования',
        choices=StudentEducationLevel.choices,
        default=StudentEducationLevel.COMPLETED_SECONDARY,
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    specialty = models.CharField(
        'специальность',
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    course_list = models.ManyToManyField(
        Course,
        related_name='student',
        through='StudentCourse',
        verbose_name='курсы студента',
    )
    hard_skills = models.ManyToManyField(
        HardSkill,
        related_name='student',
        through='StudentHardSkill',
        verbose_name='навыки студента',
    )
    status = models.CharField(
        'статус поиска работы',
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVELY_SEARCHING,
        max_length=lim.STANDARD_MAX_CHAR_FIELD_LENGTH,
    )
    image = models.ImageField(
        'фото студента',
        upload_to='students/images',
        blank=True,
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        """Возвращает полное имя студента."""
        return f'{self.first_name} {self.last_name}'

    def save(self):
        """Переопределённый метод.

        Сжимает изображение пользователя с сохранением пропорций.
        """
        super().save()
        img = Image.open(self.image.path)

        if img.height > lim.STUDENT_IMAGE_SIZE or \
           img.width > lim.STUDENT_IMAGE_SIZE:
            output_size = (lim.STUDENT_IMAGE_SIZE, lim.STUDENT_IMAGE_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path)


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
        return f'{self.student.__str__()} прошёл курс {self.course.title}'


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
        return f'{self.student.__str__()} может в {self.hard_skill.title}'
