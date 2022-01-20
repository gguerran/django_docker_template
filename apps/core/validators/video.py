import os
from django.core.exceptions import ValidationError


def validate_video(value):
    extensions = [
        "avi",
        "mp4",
        "m4v",
        "mov",
        "mpg",
        "mpeg",
        "wmv",
        ".avi",
        ".mp4",
        ".m4v",
        ".mov",
        ".mpg",
        ".mpeg",
        ".wmv",
    ]
    filename = value.name
    extension = os.path.splitext(filename)[1]
    if extension not in extensions:
        raise ValidationError("Tipo de arquivo inválido, por favor, envie um vídeo válido", params={"video": value})
