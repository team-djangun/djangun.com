from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import GamificationInterface

User = get_user_model()


@receiver(post_save, sender=User)
def auto_create_game_interface(sender, instance, created, **kwargs):
    if created:
        if not hasattr(instance, "GamificationInterface"):
            game_interface = GamificationInterface.objects.create()
            instance.gamificate = game_interface
            instance.save()
