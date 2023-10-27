from django.contrib import admin

from .models import (
    Course,
    HardSkill,
    Location,
    OfficeFormat,
    Specialty,
    Student,
    WorkFormat,
    WorkSchedule,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Админка для модели студентов."""

    list_display = (
        'first_name',
        'last_name',
        'telegram_username',
        'image',
        'activity_level',
        'current_location',
        'status',
        'display_courses',
        'work_experience',
        'created_at',
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

    def display_courses(self, obj):
        return ', '.join([course.name for course in obj.course_list.all()[:2]])

    display_courses.short_description = 'курсы'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WorkFormat)
class WorkFormatAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OfficeFormat)
class OfficeFormatAdmin(admin.ModelAdmin):
    list_display = ('name',)
