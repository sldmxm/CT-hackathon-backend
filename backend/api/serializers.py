from rest_framework import serializers
from students.models import (
    Course,
    HardSkill,
    Location,
    OfficeFormat,
    Specialty,
    Student,
    WorkFormat,
    WorkSchedule,
)
from vacancies.models import Grade, Vacancy


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


class StudentSerializer(serializers.ModelSerializer):
    """Сериализация студентов."""

    work_experience = serializers.CharField(source='display_work_experience')
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
    image = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def get_image_url(self, obj):
        """Возвращает относительный путь изображения."""
        if obj.image:
            return obj.image.url
        return None


class VacancyViewSerializer(serializers.ModelSerializer):
    """Сериализация вакансий."""

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

    image = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'

    def get_image_url(self, obj):
        """Возвращает относительный путь изображения."""
        if obj.image:
            return obj.image.url
        return None
