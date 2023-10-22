from django.contrib import admin

from .models import Course, HardSkill, Student, StudentCourse, StudentHardSkill


class StudentCourseInline(admin.TabularInline):
    """Поля для выбора курса студента."""

    model = StudentCourse
    min_num = 1
    extra = 0


class StudentHardSkillsInline(admin.TabularInline):
    """Поля для выбора навыка студента."""

    model = StudentHardSkill
    min_num = 1
    extra = 4


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Админка для модели студентов."""

    list_display = (
        'id',
        'first_name',
        'last_name',
        'location',
        'education',
        'display_courses',
        'display_hard_skills',
        'status',
        'image',
    )
    list_filter = (
        'last_name',
        'location',
        'course_list',
        'status',
    )

    search_fields = (
        r'^last_name',
        r'^location',
        r'^course_list',
        r'^course_list__title'
        r'^course_list__slug'
        r'^hard_skills__title'
        'status',
    )

    inlines = (
        StudentCourseInline,
        StudentHardSkillsInline,
    )

    def display_courses(self, obj):
        """Отображает М2М поле модели курсов."""
        return ', '.join([course.title for course in obj.course_list.all()])

    def display_hard_skills(self, obj):
        """Отображает М2М поле модели навыков."""
        return ', '.join(
            [hard_skill.title for hard_skill in obj.hard_skills.all()]
        )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка для модели курсов."""

    list_display = ('id', 'title', 'slug')
    search_fields = (r'^title', r'^slug')


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    """Админка для модели навыков."""

    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    """Админка для модели студент-курс."""

    list_display = ('student', 'course')
    search_fields = (r'^student__last_name', r'^course__title',)
    list_filter = ('student__last_name',)


@admin.register(StudentHardSkill)
class StudentHardSkillAdmin(admin.ModelAdmin):
    """Админка для модели студент-навык."""

    list_display = ('student', 'hard_skill')
    search_fields = (r'^student__last_name', r'^hard_skill__title',)
    list_filter = ('student__last_name',)
