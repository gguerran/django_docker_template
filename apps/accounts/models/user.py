from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db.models import BooleanField, CharField, EmailField

from apps.core.models import BaseModelMixin


class BaseUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def get_or_none(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None


class User(AbstractBaseUser, PermissionsMixin, BaseModelMixin):
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField("endereço de e-mail", unique=True)
    is_staff = BooleanField("status de admin", default=False)
    is_active = BooleanField("ativo", default=True)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
        ordering = ["name", "-created_at"]
