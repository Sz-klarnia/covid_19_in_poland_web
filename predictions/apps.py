from django.apps import AppConfig


class PredictionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictions'


    def ready(self):
        from .scheduler import start
        start()