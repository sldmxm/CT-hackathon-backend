from django.contrib import admin

from .models import Course, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Админка для модели студентов."""

    list_display = (
        'id',
        'first_name',
        'last_name',
        'current_location',
        'education',
        'display_courses',
        'display_hard_skills',
        'status',
        'image',
    )
    list_filter = (
        'last_name',
        'current_location',
        'course_list',
        'status',
    )

    search_fields = (
        r'^last_name',
        r'^current_location',
        r'^course_list',
        r'^course_list__name'
        r'^hard_skills__name'
        'status',
    )

    # inlines = (
    # StudentCourseInline,
    # StudentHardSkillsInline,
    # )

    def display_courses(self, obj):
        """Отображает М2М поле модели курсов."""
        return ', '.join([course.name for course in obj.course_list.all()])

    def display_hard_skills(self, obj):
        """Отображает М2М поле модели навыков."""
        return ', '.join(
            [hard_skill.name for hard_skill in obj.hard_skills.all()]
        )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка для модели курсов."""

    list_display = ('id', 'name',)
    search_fields = (r'^name',)
