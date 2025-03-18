from .models import Order
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Order)
def post_save_create_order(sender, instance, created, *args, **kwargs):
    if created:
        Order.objects.create(created_by=instance)

@receiver(post_save, sender=Order)
def save_order(sender, instance, **kwargs):
    instance.order.save()