from django import forms
from allauth.account.forms import SignupForm

from . import models
from Habits import models as habit_models


''' Interface and options when a user signs up.'''

class MyRunDate(forms.DateTimeInput):
    input_type = 'date'


class CustomSignupForm(SignupForm):

    '''The form for registration of an account'''

    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={
                "placeholder":"Enter your first name",
                "id":"string_first_name"
            }
        )
    )
    second_name = forms.CharField(
        required=False,
        label='Second name (optional)',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your second name",
                "id": "str_second_name",
            }
        )
    )

    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name",
                "id": "str_last_name",
            }
        )
    )
    date_run = forms.DateField(
        required=False,
        label='Date of the Triathlon',
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "id": "datetime_date_run",
            },
        ),
    )



    def save(self,request):
        user = super(CustomSignupForm,self).save(request)

        profile = models.Profile.objects.get(user=user)
        profile.first_name = self.cleaned_data['first_name']
        profile.second_name = self.cleaned_data['second_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.date_run = self.cleaned_data['date_run']
        profile.save()

        '''Returns 5 predefined habits after registering'''

        habit1 = habit_models.Habit.objects.create(
            author=profile,
            name="Run",
            description="2 hours",
            periodicity="7",
        )
        habit1.save()

        habit2 = habit_models.Habit.objects.create(
            author=profile,
            name="Swim",
            description="2 hours",
            periodicity="7",
        )
        habit2.save()

        habit3 = habit_models.Habit.objects.create(
                author=profile,
                name="Cycle",
                description="3 hours",
                periodicity="7",
            )
        habit3.save()

        habit4 = habit_models.Habit.objects.create(
            author=profile,
            name="Sleep",
            description="8 hours",
            periodicity="1",
        )
        habit4.save()

        habit5 = habit_models.Habit.objects.create(
            author=profile,
            name="Consult your coach",
            description=" ",
            periodicity="7",
        )
        habit5.save()

        return user
