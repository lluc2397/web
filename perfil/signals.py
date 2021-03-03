from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Perfil
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

MyUser = get_user_model()

def usuario_grupo(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='comentador')
		group.user_set.add(instance)

# signal that gets fired after the user is saved
@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=MyUser)
def save_profile(sender, instance, **kwargs):
    instance.perfil.save()
