from django.apps import AppConfig


class BookreviewAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookreview_app'

    def ready(self):
        import bookreview_app.signals