from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transact


@receiver(post_save, sender=Transact)
def post_save_create_trans_id(sender, instance, created, *args, **kwargs):
    if created:
        Transact.objects.create(created_by=instance)

@receiver(post_save, sender=Transact)
def save_transact(sender, instance, **kwargs):
    instance.transact.save()