from django.apps import AppConfig


class VisitorsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitors_app'

    def ready(self):
        import visitors_app.signals