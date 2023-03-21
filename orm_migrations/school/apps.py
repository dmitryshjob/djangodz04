from django.apps import AppConfig


class SchoolConfig(AppConfig):
    default_auto_fieid = 'django.db.models.SmallAutoField'
    name = 'school'
    verbose_name = 'Школа'
