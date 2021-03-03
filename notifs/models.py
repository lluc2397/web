from django.db import models
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class Notifs(models.Model):
    NOTIFICATION_TYPES = ((1,'Nuevo_Post'),(2,'Nuevo_Curso'))

    titulo = models.CharField(max_length=200, blank=True)
    sender = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)