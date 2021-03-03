from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from notifs.models import Notifs
from web.models import PostWeb
from django.contrib.auth import get_user_model

MyUser = get_user_model()

@receiver(post_save, sender=PostWeb)
def notif_new_post(sender, instance, *args, **kwargs):
    post = instance.title
    text_preview = instance.resumen
    sender = instance.author
    para = MyUser.objects.all()
    notify = Notifs(titulo=post, sender=sender, user=para, text_preview=text_preview ,notification_type=1)
    notify.save()

