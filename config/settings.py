from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY", default="^(u9$oqq_f#5*gql^cezg)!r)(#3(*=bu9d)%j&+o#3ea7usv#o^@6pbak@gx0q#r&0a-^xa(@")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="*", cast=Csv())

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PART_APPS = []

LOCAL_APPS = [
    "apps.accounts",
    "apps.core",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS

DJANGO_MIDDLEWARES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOCAL_MIDDLEWARES = [
    "apps.core.middlewares.RequestMiddleware",
]

MIDDLEWARE = DJANGO_MIDDLEWARES + LOCAL_MIDDLEWARES

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": config("DB_NAME", default="github-actions"),
        "USER": config("DB_USER", default="postgres"),
        "PASSWORD": config("DB_PASSWORD", default="postgres"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

AUTH_USER_MODEL = "accounts.User"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 6}},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Fortaleza"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATIC_ROOT = "/static/"

MEDIA_URL = "/media/"

MEDIA_ROOT = "media/"

EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.filebased.EmailBackend")

EMAIL_FILE_PATH = config("EMAIL_FILE_PATH", default="email-logs")

EMAIL_HOST = config("EMAIL_HOST", default="smtp.sendgrid.net")

EMAIL_PORT = config("EMAIL_PORT", default="587")

EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="no-reply@project.com")

EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="pass")

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="no-reply@project.com")

BASE_URL = config("BASE_URL", default="http://127.0.0.1:8000/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
