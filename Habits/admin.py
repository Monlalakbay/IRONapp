from django.contrib import admin

from . import models

'''This script is used to display the Habit and Tracker Models in the admin panel.'''

class TrackerModel(admin.TabularInline):
    model = models.Tracker

class HabitAdmin(admin.ModelAdmin):
    inlines = [TrackerModel]

    class Meta:
        model = models.Habit


admin.site.register(models.Habit, HabitAdmin)
admin.site.register(models.Tracker)