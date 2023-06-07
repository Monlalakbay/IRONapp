from django import forms

from . import models

'''Forms in the context of Django are used to accept and process the input of the users using the site. 
This script dictates what the user sees when interacting with their habits.'''

class HabitForm(forms.ModelForm):

    '''What the user sees on the interface when registering a new habit.'''

    name = forms.CharField(
        label='Iron Task',
        widget=forms.TextInput(
            attrs={'placeholder': 'Let´s  do this.'}
        )
    )

    description = forms.CharField(
        label='Description',
        widget = forms.TextInput(
            attrs={
                'rows':2,
                'placeholder': 'How far did you push yourself? (eg. duration of workout)',
                }
            )
    )

    periodicity = forms.CharField(
        label='Routine',
        widget=forms.Select(
            attrs={
                'style': 'width: 200px; height: 43px;',
                },
            choices=models.Habit.periodicity_choices,
            )
    )


    class Meta:

        ''' Maps out the filled-out form onto the habit model attributes.'''

        model = models.Habit
        fields = [
            'name',
            'description',
            'periodicity',
        ]