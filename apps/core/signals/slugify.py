from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify as djslugify


@receiver(pre_save)
def slugify(sender, instance, **kwargs):
    try:
        sender._meta.get_field("slug")
        instance.slug = djslugify(instance.title)
    except Exception as e:  # noqa
        pass
