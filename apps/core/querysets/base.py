from django.db.models.query import QuerySet


class BaseQuerySet(QuerySet):
    def get_or_none(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None
