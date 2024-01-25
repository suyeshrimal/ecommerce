from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Customer

user=get_user_model()
@receiver(post_save,sender=user)
def on_user_create(sender,instance,*args,**kwargs):
    Customer.objects.get_or_create(
        user=instance
    )