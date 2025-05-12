from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    # временная заглушка - для очистки сессии для авторизации
    # def ready(self):
    #     from django.contrib.sessions.models import Session
    #     Session.objects.all().delete()