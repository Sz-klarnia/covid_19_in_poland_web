from django.apps import AppConfig


class ScheduledTasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduled_tasks'

    def ready(self):
        from scheduled_tasks import schedulers
            schedulers.start()
