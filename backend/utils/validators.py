import re

from django.core.exceptions import ValidationError


def validate_telegram_username(value):
    if not re.match(r'^@[\w\d_]+$', value):
        raise ValidationError(
            'Неверное имя пользователя Telegram. '
            'Оно должно начинаться с символа '
            '"@" и может содержать только буквы, '
            'цифры и символы подчеркивания'
        )


def validate_color_format(value):
    if not re.match(r'^#[0-9a-fA-F]{3,6}$', value):
        raise ValidationError(
            'Неверный формат для цвета, должно быть #AABBCC или #ABC'
        )
