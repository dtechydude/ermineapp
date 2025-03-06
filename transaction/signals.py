from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MerchantSetTransact


@receiver(post_save, sender=MerchantSetTransact)
def post_save_create_trans_id(sender, instance, created, *args, **kwargs):
    if created:
        MerchantSetTransact.objects.create(merchant=instance)

@receiver(post_save, sender=MerchantSetTransact)
def save_merchantsettransact(sender, instance, **kwargs):
    instance.merchantsettransact.save()