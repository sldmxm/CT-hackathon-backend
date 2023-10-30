from rest_framework import serializers
from students.models import (
    Course,
    HardSkill,
    Location,
    OfficeFormat,
    Specialty,
    Student,
    StudentLanguage,
    WorkFormat,
    WorkSchedule,
)
from vacancies.models import Candidate, Grade, Vacancy


class BaseNameSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для моделей с полем 'name'."""

    class Meta:
        fields = ('name',)


class LocationSerializer(BaseNameSerializer):
    """Сериализация местоположений."""

    class Meta(BaseNameSerializer.Meta):
        model = Location


class GradeSerializer(BaseNameSerializer):
    """Сериализация грейдов."""

    class Meta(BaseNameSerializer.Meta):
        model = Grade


class WorkScheduleSerializer(BaseNameSerializer):
    """Сериализация расписаний работы."""

    class Meta(BaseNameSerializer.Meta):
        model = WorkSchedule


class WorkFormatSerializer(BaseNameSerializer):
    """Сериализация форматов работы."""

    class Meta(BaseNameSerializer.Meta):
        model = WorkFormat


class OfficeFormatSerializer(BaseNameSerializer):
    """Сериализация форматов офиса."""

    class Meta(BaseNameSerializer.Meta):
        model = OfficeFormat


class CourseSerializer(BaseNameSerializer):
    """Сериализация курсов."""

    class Meta(BaseNameSerializer.Meta):
        model = Course


class SpecialtySerializer(BaseNameSerializer):
    """Сериализация навыков."""

    class Meta(BaseNameSerializer.Meta):
        model = Specialty


class HardSkillSerializer(BaseNameSerializer):
    """Сериализация навыков."""

    class Meta(BaseNameSerializer.Meta):
        model = HardSkill


class StudentLanguageSerializer(BaseNameSerializer):
    """Сериализация языков."""

    language = serializers.StringRelatedField()

    class Meta(BaseNameSerializer.Meta):
        model = StudentLanguage
        fields = ('language', 'level',)


class StudentBriefSerializer(serializers.ModelSerializer):
    """Сокращенная сериализация студентов для канбан-доски."""

    work_experience = serializers.CharField(source='display_work_experience')
    image = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'work_experience', 'image',)

    def get_image_url(self, obj):
        """Возвращает относительный путь изображения."""
        if obj.image:
            return obj.image.url
        return None


class StudentSerializer(StudentBriefSerializer):
    """Сериализация студентов."""

    education = serializers.CharField(source='display_education')
    status = serializers.CharField(source='display_status')

    current_location = serializers.StringRelatedField()

    work_schedule = WorkScheduleSerializer(many=True, required=True)
    work_format = WorkFormatSerializer(many=True, required=True)
    office_format = OfficeFormatSerializer(many=True, required=True)
    specialty = SpecialtySerializer(many=True, required=True)
    location_to_relocate = LocationSerializer(many=True, read_only=True)
    course_list = CourseSerializer(many=True, read_only=True)
    hard_skills = HardSkillSerializer(many=True, read_only=True)
    languages = StudentLanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class StudentsMatchingVacancySerializer(StudentSerializer):
    relocation = serializers.BooleanField(default=False)
    relevant_hard_skills = HardSkillSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = (
            'id',
            'image',
            'first_name',
            'last_name',
            'office_format',
            'current_location',
            'relocation',
            'work_schedule',
            'work_experience',
            'status',
            'relevant_hard_skills',
            # остального нет в таблице на текущий момент, а стоило бы
            'specialty',
            'work_format',
        )


class VacancyBriefSerializer(serializers.ModelSerializer):
    """Сокращенная сериализация вакансий для канбан-доски."""

    image = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'title', 'image',)

    def get_image_url(self, obj):
        """Возвращает относительный путь изображения."""
        if obj.image:
            return obj.image.url
        return None


class VacancySerializer(VacancyBriefSerializer):
    """Полная сериализация вакансий."""

    location = LocationSerializer(many=True, required=True)
    grade = GradeSerializer(many=True, required=True)
    work_schedule = WorkScheduleSerializer(many=True, required=True)
    work_format = WorkFormatSerializer(many=True, required=True)
    course_list = CourseSerializer(many=True, required=True)
    hard_skill = HardSkillSerializer(many=True, required=True)

    work_experience = serializers.CharField(source='display_work_experience')
    education = serializers.CharField(source='display_education')

    office_format = serializers.StringRelatedField()
    specialty = serializers.StringRelatedField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Vacancy
        fields = '__all__'


class CandidateEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ('kanban_position', 'notes', 'score',)


class CandidateViewSerializer(serializers.ModelSerializer):
    student = StudentBriefSerializer()
    kanban_position = serializers.SlugRelatedField(
        slug_field='order_number',
        read_only=True,
    )

    class Meta:
        model = Candidate
        exclude = ('vacancy',)


class CandidateListSerializer(VacancyBriefSerializer):
    candidates = CandidateViewSerializer(many=True, read_only=True)

    class Meta(VacancyBriefSerializer.Meta):
        fields = ('id', 'title', 'image', 'candidates')


class CandidateAddSerializer(serializers.Serializer):
    """
    Сериализатор для добавления кандидатов на канбан доску.

    Формат данных:
    {"student_ids": [7,8,9]}
    """

    student_ids = serializers.ListField(
        child=serializers.IntegerField(),
    )

    def validate_students_ids(self, student_ids):
        for student_id in student_ids:
            if not isinstance(student_id, int):
                raise serializers.ValidationError(
                    'id кндидатов должны быть типа int')
        return student_ids

    def to_representation(self, instance):
        return {'student_ids': instance.student_ids}
