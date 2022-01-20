from django.contrib.admin.decorators import register
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

User = get_user_model()


@register(User)
class BaseUserAdmin(UserAdmin):
    list_display = ["name", "email", "is_active", "is_superuser"]
    list_filter = ["is_active", "is_superuser"]
    ordering = ("name", "email")

    fieldsets = [
        ["Informações pessoais", {"fields": ["name", "email"]}],
        ["Informações da conta", {"fields": ["password", "is_active", "is_superuser"]}],
    ]
    add_fieldsets = [
        ["Informações pessoais", {"fields": ["name", "email"]}],
        ["Informações da conta", {"fields": ["password1", "password2"]}],
    ]


site.unregister(Group)
