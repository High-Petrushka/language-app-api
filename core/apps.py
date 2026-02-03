from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'dango.db.models.BigAutoField'
    name = 'core'
    label = 'core'
