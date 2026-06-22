from django.apps import AppConfig

class PeopleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.people'          # ← CHANGE THIS FROM 'people' TO 'apps.people'
    verbose_name = 'People'