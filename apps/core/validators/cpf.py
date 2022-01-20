import re

from django.core.exceptions import ValidationError


def validate_cpf(value):
    exception = ValidationError("CPF inválido.", params={"document": value})
    list_cpf = list(map(int, list(re.sub(r"[^0-9]", "", value))))

    if not list_cpf or len(list_cpf) != 11:
        raise exception

    list_without_digits = list_cpf[:-2]
    first_range = list(range(10, 1, -1))
    first_digit = 11 - sum([a * b for a, b in zip(list_without_digits, first_range)]) % 11
    first_digit = 0 if first_digit > 9 else first_digit
    list_with_first_digit = list_without_digits + [first_digit]
    last_range = list(range(11, 1, -1))
    last_digit = 11 - sum([a * b for a, b in zip(list_with_first_digit, last_range)]) % 11
    new_cpf = list_with_first_digit + [last_digit]
    if new_cpf != list_cpf or list_cpf == [list_cpf[0]] * 11:
        raise exception
