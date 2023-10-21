from PIL import Image
from django.db import models


class Course(models.Model):
    """
    Модель курсов, которые прошел студент. Задействована в М2М модели
    StudentCourse
    """

    title = models.CharField('название курса', max_length=100)
    slug = models.SlugField('слаг курса', max_length=255, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return self.title


class HardSkill(models.Model):
    """
    Модель навыков, которыми обладает студент (его hard skills).
    Задействована в М2М модели StudentHardSkills
    """

    title = models.CharField('навыки студента', max_length=100)

    class Meta:
        ordering = ['title']
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'

    def __str__(self):
        return self.title


class StudentEducationLevel(models.TextChoices):
    """
    Вспомогательный класс для выбора уровня образования
    студента из ограниченного списка
    """

    INCOMPLETE_SECONDARY = 'НЕОКОЧЕННОЕ СРЕДНЕЕ'
    COMPLETED_SECONDARY = 'СРЕДНЕЕ'
    SECONDARY_PROFESSIONAL = 'СРЕДНЕЕ ПРОФЕССИОНАЛЬНОЕ'
    INCOMPLETE_HIGHER = 'НЕОКОНЧЕННОЕ ВЫСШЕЕ'
    COMPLETED_HIGHER = 'ВЫСШЕЕ'


class StudentStatus(models.TextChoices):
    """
    Вспомогательный класс для выбора статуса студента
    в карьерном трекере
    """

    EMPLOYMENT_COURSE = 'КУРС ПО ТРУДОУСТРОЙСТВУ'
    PREACCELERATION = 'ПРЕАКСЕЛЕРАЦИЯ'
    ACCELERATION = 'АКСЕЛЕРАЦИЯ'
    EMPLOYED = 'ТРУДОСУСТРОЕН'
    EXPELLED = 'ОТЧИСЛЕН'


class Student(models.Model):
    """
    Модель для хранения информации о студенте
    """

    first_name = models.CharField(
        'имя студента',
        max_length=100,
    )
    last_name = models.CharField(
        'фамилия студента',
        max_length=100,
    )
    location = models.CharField(
        'местоположение',
        max_length=100,
    )
    education = models.CharField(
        'уровень образования',
        choices=StudentEducationLevel.choices,
        default=StudentEducationLevel.COMPLETED_SECONDARY,
        max_length=100,
    )
    specialty = models.CharField(
        'специальность',
        max_length=100,
        blank=True,
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
        'статус в трекере',
        choices=StudentStatus.choices,
        default=StudentStatus.ACCELERATION,
        max_length=100,
    )
    image = models.ImageField(
        'фото студента',
        upload_to='students/images',
        blank=True,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self):
        """
        Переопределённый метод для сжатия изображения пользователя
        с сохранением пропорций.
        """

        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StudentCourse(models.Model):
    """
    Модель для связи студентов и курсов
    """

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='student_course',
        verbose_name='студент курса'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='course_student',
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
        return f'{self.student.__str__()} прошёл курс {self.course.title}'


class StudentHardSkill(models.Model):
    """
    Модель для связи студентов и навыков
    """

    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        related_name='student_skill',
        verbose_name='студенческий навык'
    )
    hard_skill = models.ForeignKey(
        HardSkill,
        on_delete=models.PROTECT,
        related_name='skill_student',
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
        return f'{self.student.__str__()} может в {self.hard_skill.title}'
