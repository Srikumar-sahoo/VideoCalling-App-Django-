from django.apps import AppConfig


class MyBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_base'
