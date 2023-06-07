from . import models


''' Retrieves the date run and makes it easily accessible to calculate the countdown'''

def profile_daterun(request):
    if request.user.is_authenticated:
        profile_obj = models.Profile.objects.get(user=request.user)
        run = profile_obj.date_run
        dic = {
            'daterun': run,
        }
        return dic
    return {}
