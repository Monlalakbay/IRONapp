from django.db.models import Q
import datetime as dt
from . import models

'''The module that calculates when a tally should be saved and the streak to be increased or reset.'''

def analyse( qs_h, now ):
    qs_t_model = models.Tracker.objects.filter(
        Q(counter=qs_h)
    ).order_by('-created').first()

    condition = 0
    flag = False
    if (qs_t_model is not None):
        qs_t = qs_t_model.created
        streak = qs_t_model.streak
        qs_t_day = dt.date(qs_t.year, qs_t.month, qs_t.day)

        '''Checks if the habit that the logged-in user did is within the periodicity they registered it with.
        If yes, the habit streak will be increased, if it's less then it wont be saved and the streak remains the same. 
        If the habit is accomplished after the periodicity, then the streak resets to 1. '''

        print(qs_t_day)
        if (qs_t_day < now.date()):
            if (qs_t_day + dt.timedelta(days=int(qs_h.periodicity)) == now.date()):
                streak = streak + 1
                flag = True
            elif (now.date() > qs_t_day + dt.timedelta(days=int(qs_h.periodicity))):
                streak = 1
                flag = True
                condition = 1
            else:
                condition = 2
    else:
        print("test none")
        streak = 1
        flag = True

    if (flag == True):
        tally = models.Tracker.objects.create(
            created = now,
            counter=qs_h,
            streak=streak,
        )
        tally.save()
    return streak, flag, condition