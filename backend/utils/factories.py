import random

from factory import LazyAttribute, LazyFunction
from factory.django import DjangoModelFactory
from faker import Faker
from students.models import (
    Course,
    HardSkill,
    Language,
    Location,
    OfficeFormat,
    Specialty,
    Student,
    StudentLanguage,
    WorkFormat,
    WorkSchedule,
)
from users.models import User
from utils import constants
from vacancies.models import Grade, Kanban, Vacancy, VacancyStudent

from backend.constants import (
    EDUCATION_LEVEL_CHOICES,
    EXPERIENCE_CHOICES,
    LANGUAGE_LEVEL_CHOICES,
    WORK_SEEKING_STATUS_CHOICES,
)

fake = Faker('ru_RU')


class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    email = LazyFunction(fake.email)
    telegram_username = LazyAttribute(lambda _: f'@{fake.user_name()}')
    salary_from = LazyFunction(
        lambda: random.randint(
            constants.STUDENT_MIN_SALARY,
            constants.STUDENT_MAX_SALARY
        )
        if random.choice([True, False]) else None
    )
    activity_level = LazyFunction(lambda: random.randint(0, 100))
    portfolio_link = LazyFunction(
        lambda: constants.STUDENT_PORTFOLIO_URL
        if random.choice([True, False]) else None
    )
    resume_link = LazyFunction(
        lambda: constants.STUDENT_RESUME_URL
        if random.choice([True, False]) else None
    )

    current_location = LazyAttribute(
        lambda _: random.choice(Location.objects.all()))
    education = LazyFunction(
        lambda: random.choice(EDUCATION_LEVEL_CHOICES)[0])
    status = LazyFunction(
        lambda: random.choice(WORK_SEEKING_STATUS_CHOICES)[0])
    work_experience = LazyFunction(
        lambda: random.choice(EXPERIENCE_CHOICES)[0])

    @classmethod
    def get_random_items(cls, model, min_count, max_count):
        count = random.randint(min_count, max_count)
        return list(model.objects.order_by('?')[:count])

    @classmethod
    def create(cls, **kwargs):
        """Создание записей M2M с уже заполненным моделями."""

        student = super().create(**kwargs)

        student.location_to_relocate.set(
            cls.get_random_items(
                Location,
                constants.LOCATION_TO_RELOCATE_MIN,
                constants.LOCATION_TO_RELOCATE_MAX
            )
        )
        student.hard_skills.set(
            cls.get_random_items(
                HardSkill,
                constants.STUDENT_HARD_SKILLS_MIN,
                constants.STUDENT_HARD_SKILLS_MAX
            )
        )
        student.course_list.set(
            cls.get_random_items(
                Course,
                constants.STUDENT_COURSES_MIN,
                constants.STUDENT_COURSES_MAX
            )
        )
        student.specialty.set(
            cls.get_random_items(
                Specialty,
                constants.STUDENT_SPECIALITY_MIN,
                constants.STUDENT_SPECIALITY_MAX
            )
        )
        student.work_schedule.set(
            cls.get_random_items(
                WorkSchedule,
                constants.STUDENT_WORK_SCHEDULE_MIN,
                constants.STUDENT_WORK_SCHEDULE_MAX
            )
        )
        student.work_format.set(
            cls.get_random_items(
                WorkFormat,
                constants.STUDENT_WORK_FORMAT_MIN,
                constants.STUDENT_WORK_FORMAT_MAX
            )
        )
        student.office_format.set(
            cls.get_random_items(
                OfficeFormat,
                constants.STUDENT_OFFICE_FORMAT_MIN,
                constants.STUDENT_OFFICE_FORMAT_MAX
            )
        )

        StudentLanguage.objects.create(
            student=student,
            language=random.choice(Language.objects.all()),
            level=random.choice(LANGUAGE_LEVEL_CHOICES)[0]
        )
        return student


class VacancyFactory(DjangoModelFactory):
    class Meta:
        model = Vacancy

    specialty = LazyAttribute(
        lambda _: random.choice(Specialty.objects.all()))
    title = specialty
    description = LazyFunction(fake.text)
    company = LazyFunction(fake.company)
    is_published = LazyFunction(lambda: random.choice([True, False]))
    is_active = LazyFunction(lambda: random.choice([True, False]))
    salary_from = LazyFunction(
        lambda: random.randint(
            constants.VACANCY_MIN_SALARY,
            (constants.VACANCY_MIN_SALARY + constants.VACANCY_MAX_SALARY) // 2
        )
        if random.choice([True, False]) else None
    )
    salary_to = LazyFunction(
        lambda: random.randint(
            (constants.VACANCY_MIN_SALARY + constants.VACANCY_MAX_SALARY) // 2,
            constants.VACANCY_MAX_SALARY
        )
        if random.choice([True, False]) else None
    )

    author = LazyAttribute(
        lambda _: random.choice(User.objects.all()))
    specialty = LazyAttribute(
        lambda _: random.choice(Specialty.objects.all()))
    office_format = LazyAttribute(
        lambda _: random.choice(OfficeFormat.objects.all()))

    work_experience = LazyFunction(
        lambda: random.choice(EXPERIENCE_CHOICES)[0])
    education = LazyFunction(
        lambda: random.choice(EDUCATION_LEVEL_CHOICES)[0])

    language = LazyAttribute(
        lambda _: random.choice(Language.objects.all()))
    language_level = LazyFunction(
        lambda: random.choice(LANGUAGE_LEVEL_CHOICES)[0])

    @classmethod
    def get_random_items(cls, model, min_count, max_count):
        count = random.randint(min_count, max_count)
        return list(model.objects.order_by('?')[:count])

    @classmethod
    def create(cls, **kwargs):
        """Создание записей M2M с уже заполненным моделями."""

        vacancy = super().create(**kwargs)
        vacancy.location.set(
            cls.get_random_items(
                Location,
                constants.VACANCY_LOCATIONS_MIN,
                constants.VACANCY_LOCATIONS_MAX
            )
        )
        vacancy.grade.set(
            cls.get_random_items(
                Grade,
                constants.VACANCY_GRADES_MIN,
                constants.VACANCY_GRADES_MAX
            )
        )
        vacancy.hard_skill.set(
            cls.get_random_items(
                HardSkill,
                constants.VACANCY_HARD_SKILLS_MIN,
                constants.VACANCY_HARD_SKILLS_MAX
            )
        )
        vacancy.work_schedule.set(
            cls.get_random_items(
                WorkSchedule,
                constants.VACANCY_WORK_SCHEDULE_MIN,
                constants.VACANCY_WORK_SCHEDULE_MAX,
            )
        )
        vacancy.work_format.set(
            cls.get_random_items(
                WorkFormat,
                constants.VACANCY_WORK_FORMAT_MIN,
                constants.VACANCY_WORK_FORMAT_MAX
            )
        )
        vacancy.course_list.set(
            cls.get_random_items(
                Course,
                constants.VACANCY_COURSES_MIN,
                constants.VACANCY_COURSES_MAX
            )
        )
        return vacancy


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = LazyFunction(fake.user_name)
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)


class VacancyStudentFactory(DjangoModelFactory):
    class Meta:
        model = VacancyStudent

    student = LazyAttribute(
        lambda _: random.choice(Student.objects.all()))
    vacancy = LazyAttribute(
        lambda _: random.choice(Vacancy.objects.all()))
    score = LazyFunction(lambda: random.randint(1, 5))
    notes = LazyFunction(fake.text)
    kanban_position = LazyAttribute(
        lambda _: random.choice(Kanban.objects.all()))
