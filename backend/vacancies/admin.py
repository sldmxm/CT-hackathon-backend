from django.contrib import admin

from .models import Filter, Vacancy, VacancyStudents


class FilterInline(admin.TabularInline):
    model = Filter
    extra = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_active', 'is_published')
    list_filter = ('is_active', 'is_published')
    search_fields = ('title', 'author__username', 'company', 'city')
    list_per_page = 20

    inlines = [FilterInline]

    fieldsets = [
        ('Основная информация', {
            'fields': (
                'title',
                'author',
                'description',
                'salary_from',
                'salary_to',
                'city',
                'company',
            )
        }),
        ('Состояние и видимость', {
            'fields': (
                'is_active',
                'is_published'
            ),
        }),
        ('Дата создания и обновления', {
            'fields': (
                'created_at',
                'updated_at'
            ),
            'classes': (
                'collapse',
            ),
        }),
    ]

    readonly_fields = ('created_at', 'updated_at')


@admin.register(VacancyStudents)
class VacancyStudentsAdmin(admin.ModelAdmin):
    list_display = ('student', 'vacancy', 'score')
    list_filter = ('vacancy',)
    search_fields = (
        'student__first_name',
        'student__last_name',
        'vacancy__title',
    )
    list_per_page = 20

    fieldsets = [
        ('Информация о студенте и вакансии', {
            'fields': ('student', 'vacancy', 'score')
        }),
        ('Заметки HR', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('student', 'vacancy')
        return queryset