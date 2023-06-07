from django.apps import AppConfig

'''The script that allows the django framework to interact with the Habits app for configuration.'''

class HabitsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Habits"
