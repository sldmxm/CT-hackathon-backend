from django.contrib import admin

from .models import Course, HardSkill, Student, StudentCourse, StudentHardSkill


class StudentCourseInline(admin.TabularInline):
    model = StudentCourse
    min_num = 1
    extra = 0


class StudentHardSkillsInline(admin.TabularInline):
    model = StudentHardSkill
    min_num = 1
    extra = 4


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
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
        return ', '.join([course.title for course in obj.course_list.all()])

    def display_hard_skills(self, obj):
        return ', '.join(
            [hard_skill.title for hard_skill in obj.hard_skills.all()]
        )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = (r'^title', r'^slug')


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')
    search_fields = (r'^student__last_name', r'^course__title',)
    list_filter = ('student__last_name',)


@admin.register(StudentHardSkill)
class StudentHardSkillAdmin(admin.ModelAdmin):
    list_display = ('student', 'hard_skill')
    search_fields = (r'^student__last_name', r'^hard_skill__title',)
    list_filter = ('student__last_name',)
