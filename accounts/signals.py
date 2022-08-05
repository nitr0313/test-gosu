from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_profile_object(sender, instance, *args, **kwargs):
    """
    Создание Объекта при создании пользователя
    """
    obj_ = Profile.objects.filter(user=instance).first()
    if obj_ is None:
        Profile.objects.create(user=instance)
