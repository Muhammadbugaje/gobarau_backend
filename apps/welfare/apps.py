from django.apps import AppConfig

class WelfareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.welfare'          # ← CHANGE THIS FROM 'welfare' TO 'apps.welfare'
    verbose_name = 'Welfare'