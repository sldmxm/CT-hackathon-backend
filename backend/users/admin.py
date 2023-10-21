from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = (
        'username',
    )
    list_filter = (
        'username',
    )
    search_fields = (
        'username',
    )
