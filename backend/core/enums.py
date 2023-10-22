"""Определение константных значений.

Применена библиотека Enum
"""

from enum import IntEnum


class Limits(IntEnum):
    """Определение констант для максимальных значений."""

    STANDARD_MAX_CHAR_FIELD_LENGTH = 150
    STUDENT_IMAGE_SIZE = 300
