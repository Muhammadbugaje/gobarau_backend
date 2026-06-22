from django.apps import AppConfig

class AcademicsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics'          # ← CHANGE THIS FROM 'academics' TO 'apps.academics'
    verbose_name = 'Academics'