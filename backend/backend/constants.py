STANDARD_MAX_CHAR_FIELD_LENGTH = 150
SMALL_IMAGE_SIZE = 300
MIN_SALARY = 0
EXPERIENCE_CHOICES = (
    (0, 'Без опыта'),
    (0.4, 'Менее 6 месяцев'),
    (0.9, 'Менее года'),
    (1, 'Один год'),
    (2, 'Два года'),
    (3, 'Три года'),
    (4, 'Четыре года'),
    (5, 'Пять лет'),
    (5.1, 'Более пяти лет'),
)
EDUCATION_LEVEL_CHOICES = (
    (0, 'Неоконченное среднее'),
    (1, 'Среднее образование'),
    (2, 'Среднее профессиональное'),
    (3, 'Бакалавр'),
    (4, 'Магистр'),
    (5, 'Докторантура'),
)
WORK_SEEKING_STATUS_CHOICES = (
    ('actively_seeking', 'Активно ищу работу'),
    ('additional_work', 'Ищу дополнительную работу'),
    ('passively_seeking', 'Пассивно ищу работу'),
    ('open_to_offers', 'Открыт для предложений'),
    ('not_seeking', 'Не ищу работу'),
)
FILTER_FIELDS_FOR_VACANCY_CHOICES = (
    ('salary_from', 'зарплата от'),
    ('salary_to', 'зарплата до'),
    ('activity_level', 'активность'),
    ('created_at', 'дата создания'),
    ('updated_at', 'дата изменения'),
    ('current_location', 'местонахождение'),
    ('location_to_relocate', 'местонахождения для переезда'),
    ('course_list', 'курсы'),
    ('hard_skills', 'навыки'),
    ('specialty', 'специальность'),
    ('employment', 'виды занятости'),
    ('work_schedule', 'графики работы'),
    ('work_format', 'форматы работы'),
    ('office_format', 'форматы места работы'),
    ('education', 'уровень образования'),
    ('work_experience', 'опыт работы')
)
