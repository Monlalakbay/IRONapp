from django.db import models
from django.contrib.auth.models import User

from UserProfile.models import Profile
from django.utils import timezone


'''The app has two tables: One documenting the habits created. 
Another one, tallying when the habits are done by the user.'''


class Habit(models.Model):

    '''Dictates how the table in the db for Habits is organized. When a user registers a new habit,
     the following attributes are saved.'''

    created = models. DateTimeField(default=timezone.now, blank=True, null=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='habits')

    name = models.CharField(max_length=20)
    description = models.TextField()
    periodicity_choices = (
        ('1','Daily'),
        ('7','Weekly'),
    )
    periodicity = models.CharField(max_length=7, choices=periodicity_choices)

    '''These attributes are included so they may be easily accessible to the main.html'''

    def cur_streak(self):
        '''The current streak is the streak number of the most recent saved object in the Tracker Model. '''

        cur = 0
        tmp = self.tracker_set.order_by('-created')
        if (len(tmp) > 0):
            cur = tmp[0].streak
        return cur

    def max_streak(self):

        '''The longest streak is the highest number
        (at the top of the db table) on the streak attribute in the Tracker Model.'''

        max = 0
        tmp = self.tracker_set.order_by('-streak')
        if (len(tmp) > 0):
            max = tmp[0].streak
        return max

    class Meta:

        '''This nested class gives the Habit model metadata and makes it easier for the logs to be
        read in the admin page; by giving a human-readable label and making the habits chronological. '''

        verbose_name_plural = 'Habit'
        ordering = ('-created',)

    def __str__(self):

        '''Labels each habit log in the admin page by its name and date created'''

        return str(self.author) +" - "+ self.name + ' - ' + str(self.created.strftime('%d/%m/%y'))


class Tracker(models.Model):

    '''A separate table that records the date and counts the number of times when the user does a habit.'''

    created = models.DateTimeField(default=timezone.now)
    counter = models.ForeignKey(Habit, on_delete=models.CASCADE)
    streak = models.IntegerField(default=1)


    class Meta:

        '''Labels the Tracker table and orders each log on the date created'''

        verbose_name_plural = 'Tracker'
        ordering = ('-created',)

    def __str__(self):

        '''Labels each habit log in the admin page by its name and date created'''

        return str(self.counter.author) + ' - ' +str(self.counter.name) + ' - ' + str(self.created.strftime('%d/%m/%y'))