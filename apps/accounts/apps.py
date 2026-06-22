from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'          # ← CHANGE THIS FROM 'accounts' TO 'apps.accounts'
    verbose_name = 'Accounts'