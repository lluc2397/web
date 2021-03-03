from django.apps import AppConfig
from django.db.models.signals import post_save

class PerfilConfig(AppConfig):
    name = 'perfil'

    def ready(self):
        from usuario.models import MyUser
        from .signals import usuario_grupo        
        post_save.connect(usuario_grupo, sender=MyUser)
