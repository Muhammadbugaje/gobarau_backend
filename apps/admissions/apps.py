from django.apps import AppConfig

class AdmissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.admissions'          # ← CHANGE THIS FROM 'admissions' TO 'apps.admissions'
    verbose_name = 'Admissions'