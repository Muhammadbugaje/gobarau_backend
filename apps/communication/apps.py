from django.apps import AppConfig

class CommunicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.communication'          # ← CHANGE THIS FROM 'communication' TO 'apps.communication'
    verbose_name = 'Communication'