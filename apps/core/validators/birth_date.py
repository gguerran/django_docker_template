from django.core.exceptions import ValidationError
from django.utils.timezone import now


def validate_birth_date(value):
    age = (now().date() - value).days / 365
    if age < 16:
        raise ValidationError(
            "A idade mínima para cadastro é de 16 anos.",
            params={"birth_date": value},
        )
