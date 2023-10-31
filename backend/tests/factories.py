import factory
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
from utils.factories import UserFactory
from vacancies.models import Candidate, Filter, Grade, Kanban, Vacancy

from backend.constants import (
    EDUCATION_LEVEL_CHOICES,
    EXPERIENCE_CHOICES,
    LANGUAGE_LEVEL_CHOICES,
    MIN_SALARY,
    WORK_SEEKING_STATUS_CHOICES,
)


class LanguageFactory(factory.Factory):
    class Meta:
        model = Language


class OfficeFormatFactory(factory.Factory):
    class Meta:
        model = OfficeFormat


class WorkFormatFactory(factory.Factory):
    class Meta:
        model = WorkFormat


class WorkScheduleFactory(factory.Factory):
    class Meta:
        model = WorkSchedule


class SpecialtyFactory(factory.Factory):
    class Meta:
        model = Specialty


class LocationFactory(factory.Factory):
    class Meta:
        model = Location


class HardSkillFactory(factory.Factory):
    class Meta:
        model = HardSkill


class CourseFactory(factory.Factory):
    class Meta:
        model = Course


class StudentFactory(factory.Factory):
    class Meta:
        model = Student

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    telegram_username = factory.Faker('user_name')
    salary_from = factory.Faker('random_int', min=1000, max=10000)
    activity_level = factory.Faker('random_int', min=0, max=100)
    current_location = factory.SubFactory(LocationFactory)
    education = factory.Faker(
        'random_element', elements=[choice[0]
                                    for choice in EDUCATION_LEVEL_CHOICES])
    status = factory.Faker(
        'random_element', elements=[choice[0]
                                    for choice in WORK_SEEKING_STATUS_CHOICES])
    work_experience = factory.Faker(
        'random_element', elements=[choice[0]
                                    for choice in EXPERIENCE_CHOICES])
    resume_link = factory.Faker('url')
    portfolio_link = factory.Faker('url')

    @factory.post_generation
    def location_to_relocate(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for location in extracted:
                self.location_to_relocate.add(location)

    @factory.post_generation
    def course_list(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for course in extracted:
                self.course_list.add(course)

    @factory.post_generation
    def hard_skills(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for skill in extracted:
                self.hard_skills.add(skill)

    @factory.post_generation
    def specialty(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for spec in extracted:
                self.specialty.add(spec)

    @factory.post_generation
    def work_schedule(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for schedule in extracted:
                self.work_schedule.add(schedule)

    @factory.post_generation
    def work_format(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for format in extracted:
                self.work_format.add(format)

    @factory.post_generation
    def office_format(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for format in extracted:
                self.office_format.add(format)

    @factory.post_generation
    def language(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for lang in extracted:
                level = factory.Faker(
                    'random_element',
                    elements=[choice[0]
                              for choice in LANGUAGE_LEVEL_CHOICES])
                StudentLanguageFactory(
                    student=self, language=lang, level=level)


class StudentLanguageFactory(factory.Factory):
    class Meta:
        model = StudentLanguage


class GradeFactory(factory.Factory):
    class Meta:
        model = Grade


class FilterFactory(factory.Factory):
    class Meta:
        model = Filter


class KanbanFactory(factory.Factory):
    class Meta:
        model = Kanban


class CandidateFactory(factory.Factory):
    class Meta:
        model = Candidate


class VacancyFactory(factory.Factory):
    class Meta:
        model = Vacancy

    title = factory.Faker('job')
    author = factory.SubFactory(UserFactory)
    description = factory.Faker('text')
    salary_from = factory.Faker('random_int', min=MIN_SALARY, max=10000)
    salary_to = factory.Faker('random_int', min=MIN_SALARY, max=10000)
    company = factory.Faker('company')
    is_active = factory.Faker('random_element', elements=[True, False])
    is_published = factory.Faker('random_element', elements=[True, False])
    image = factory.Faker('file_path', extension='jpg')
    portfolio = factory.Faker('random_element', elements=[True, False])
    specialty = factory.SubFactory(SpecialtyFactory)
    office_format = factory.SubFactory(OfficeFormatFactory)
    language = factory.SubFactory(LanguageFactory)
    language_level = factory.Faker(
        'random_element',
        elements=[choice[0] for choice in LANGUAGE_LEVEL_CHOICES]
    )
    work_experience = factory.Faker(
        'random_element',
        elements=[choice[0] for choice in EXPERIENCE_CHOICES]
    )
    education = factory.Faker(
        'random_element',
        elements=[choice[0] for choice in EDUCATION_LEVEL_CHOICES]
    )

    @factory.post_generation
    def location(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for loc in extracted:
                self.location.add(loc)

    @factory.post_generation
    def grade(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for grd in extracted:
                self.grade.add(grd)

    @factory.post_generation
    def hard_skill(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for skill in extracted:
                self.hard_skill.add(skill)

    @factory.post_generation
    def work_schedule(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for schedule in extracted:
                self.work_schedule.add(schedule)

    @factory.post_generation
    def work_format(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for format in extracted:
                self.work_format.add(format)

    @factory.post_generation
    def course_list(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for course in extracted:
                self.course_list.add(course)
