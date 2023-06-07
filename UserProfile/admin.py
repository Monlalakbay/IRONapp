from django.contrib import admin

from . import models


'''This file is used to display the user profiles in the admin panel.'''

admin.site.register(models.Profile)
