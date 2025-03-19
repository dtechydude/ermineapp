from .models import Ticket
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Order)
def post_save_create_ticket(sender, instance, created, *args, **kwargs):
    if created:
        Ticket.objects.create(created_by=instance)

@receiver(post_save, sender=Ticket)
def save_ticket(sender, instance, **kwargs):
    instance.ticket.save()