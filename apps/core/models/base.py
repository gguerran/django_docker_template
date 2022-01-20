import uuid

from django.db.models import Model
from django.db.models.fields import UUIDField, DateTimeField
from django.db.models.fields.related import ForeignKey, CASCADE

from apps.core.querysets import BaseQuerySet


class BaseModelMixin(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = ForeignKey(
        to="accounts.User",
        verbose_name="criado por",
        on_delete=CASCADE,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    modified_by = ForeignKey(
        to="accounts.User",
        verbose_name="modificado por",
        on_delete=CASCADE,
        related_name="%(class)s_modified_by",
        null=True,
        blank=True,
    )
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class BaseModel(BaseModelMixin):
    objects = BaseQuerySet.as_manager()

    def __str__(self) -> str:
        try:
            return self.title
        except:  # noqa
            return super().__str__()

    class Meta:
        abstract = True
