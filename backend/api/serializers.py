from rest_framework import serializers
from students.models import Course, HardSkill, Student

# StudentCourse


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курсов."""

    class Meta:
        model = Course
        fields = ('id', 'title', 'slug')


class HardSkillSerializer(serializers.ModelSerializer):
    """Сериализация навыков."""

    class Meta:
        model = HardSkill
        fields = ('title',)


# class StudentCourseSerializer(serializers.ModelSerializer):
#     """Сериализация курсов студента."""
#
#     id = serializers.ReadOnlyField(source='course.id')
#     title = serializers.ReadOnlyField(source='course.title')
#     slug = serializers.ReadOnlyField(source='course.slug')
#
#     class Meta:
#         model = StudentCourse
#         fields = ('id', 'title', 'slug')
#         validators = (
#             UniqueTogetherValidator(
#                 queryset=StudentCourse.objects.all(),
#                 fields=('student', 'course',)
#             ),
#         )


class StudentSerializer(serializers.ModelSerializer):
    """Сериализация студентов."""

    course_list = CourseSerializer(many=True, required=True)
    hard_skills = HardSkillSerializer(many=True, required=True)
    image = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'location',
            'education',
            'specialty',
            'course_list',
            'hard_skills',
            'status',
            'image',
        )

    def get_image_url(self, obj):
        """Возвращает относительный путь изображения."""
        if obj.image:
            return obj.image.url
        return None
