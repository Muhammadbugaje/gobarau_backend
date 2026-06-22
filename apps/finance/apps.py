from django.apps import AppConfig

class FinanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.finance'          # ← CHANGE THIS FROM 'finance' TO 'apps.finance'
    verbose_name = 'Finance'