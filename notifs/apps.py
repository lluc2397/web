from django.apps import AppConfig
from django.db.models.signals import post_save


class NotifsConfig(AppConfig):
    name = 'notifs'

    def ready(self):
        from web.models import PostWeb
        from .signals import notif_new_post        
        post_save.connect(notif_new_post, sender=PostWeb)
