from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = (
        'username', 'first_name', 'last_name',
    )
    list_filter = (
        'username',
    )
    search_fields = (
        'username', 'first_name', 'last_name',
    )
