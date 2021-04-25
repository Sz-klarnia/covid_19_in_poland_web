from django.apps import AppConfig


# Overriden ready method to include scheduled task starting on app start
class PredictionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predictions'

    # starting app with scheduled task
    def ready(self):
        from .scheduler import start
        start()