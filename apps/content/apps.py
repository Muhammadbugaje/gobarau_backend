from django.apps import AppConfig

class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.content'          # ← CHANGE THIS FROM 'content' TO 'apps.content'
    verbose_name = 'Content'