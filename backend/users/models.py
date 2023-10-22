from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

import backend.constants as constants


class User(AbstractUser):
    username = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        unique=True,
        verbose_name='Логин',
        validators=(
            UnicodeUsernameValidator(),
        )
    )
    first_name = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='Имя',
        validators=(
            UnicodeUsernameValidator(),
        )
    )
    last_name = models.CharField(
        max_length=constants.STANDARD_MAX_CHAR_FIELD_LENGTH,
        verbose_name='Фамилия',
        validators=(
            UnicodeUsernameValidator(),
        )
    )

    REQUIRED_FIELDS = ()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
