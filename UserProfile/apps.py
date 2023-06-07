from django.apps import AppConfig


'''The script that allows the django framework to interact with the UserProfile app for configuration.'''

class UserprofileConfig(AppConfig):

    '''To create and run a migration, to update the database and alter the id field on the models of the UserProfile app. '''

    default_auto_field = "django.db.models.BigAutoField"
    name = "UserProfile"

    def ready(self):
        import UserProfile.signals
