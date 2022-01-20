from django.db.models.fields import CharField

from apps.core.validators import validate_phone


class PhoneField(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_length = 17
        self.validators.append(validate_phone)
