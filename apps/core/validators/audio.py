import os
from django.core.exceptions import ValidationError


def validate_audio(value):
    extensions = ["mp3", "wav", "aac", "ogg", ".mp3", ".wav", ".aac", ".ogg"]
    filename = value.name
    extension = os.path.splitext(filename)[1]
    if extension not in extensions:
        raise ValidationError("Tipo de arquivo inválido, por favor, envie um áudio válido", params={"audio": value})
