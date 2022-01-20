from phonenumbers import is_valid_number, parse, is_possible_number

from django.core.exceptions import ValidationError


def validate_phone(value):
    try:
        if not is_valid_number(parse(value)) or not is_possible_number(parse(value)):
            raise ValidationError("Número de telefone inválido.", params={"phone": value})
    except:  # noqa
        raise ValidationError("Número de telefone inválido.", params={"phone": value})
