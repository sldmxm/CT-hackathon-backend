from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=settings.STANDARD_MAX_CHAR_FIELD_LENGTH,
        unique=True,
        verbose_name='User name',
        validators=[
            UnicodeUsernameValidator(),
        ]
    )

    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('username',)
