from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from . import models, forms, analysis
from UserProfile.models import Profile

import os


'''The views function takes the web request and returns a web response. 
This is the python script to get, post, tally, and delete habits.'''

class habit_list_view(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):

        '''Retrieves a habit based on the logged-in user.'''

        logged_in_user = self.request.user
        profile = Profile.objects.get(user=logged_in_user)

        '''Retrieves weekly habits.'''
        qs_w = models.Habit.objects.filter(
            Q(author=profile) & Q(periodicity="7")
        ).order_by('-created').distinct()

        '''Retrieves daily habits.'''
        qs_d = models.Habit.objects.filter(
            Q(author=profile) & Q(periodicity="1")
        ).order_by('-created').distinct()

        '''The empty habit form that user must input into. '''
        h_form = forms.HabitForm()

        '''A rendered html file returned to the user with the queried habit and its attributes.'''
        template = os.path.join('Habits', 'main.html')
        context = {
            'profile': profile,
            'h_form': h_form,
            'qs_w': qs_w,
            'qs_d': qs_d,
        }

        return render(request, template, context=context)


    def post(self, request, *args, **kwargs):

        '''Saves a new habit and tallies an existing habit of a logged-in user.'''

        logged_in_user = self.request.user
        profile = Profile.objects.get(user=logged_in_user)

        if ('submit_h_form' in request.POST):

            '''Check if the info provided of the user is valid then saves the added habit object into db.'''

            h_form = forms.HabitForm(request.POST)
            if (h_form.is_valid()):
                instance = h_form.save(commit=False)
                instance.author = profile
                instance.save()
                messages.success(self.request, 'Iron task added!')


        if ('submit_t_form' in request.POST):

            '''Retrieves the habits, connects it to the analysis module, returns messages to the user.'''

            idx = request.POST.get('submit_t_form')
            qs_h = models.Habit.objects.get(id=idx)

            now = timezone.now()
            streak, flag, condition = analysis.analyse( qs_h, now )

            if ( condition == 1):
                messages.warning(self.request,
                             'Time´s up! You failed to complete your task in the expected time.')
            elif ( condition == 2 ):
                messages.error(self.request, str(qs_h.name) + ' can only be done every after '
                               + str(qs_h.periodicity) + ' day(s).')

            if (flag==True):
                messages.success(self.request, 'Your current streak for '
                                 + str(qs_h.name) + ' is ' + str(streak) + '.')
        return redirect('habit-list')


class habit_delete_view(LoginRequiredMixin, View):

    ''' Deletes the habit in db and redirects to the habit list.'''

    def get(self, request, *args, **kwargs):
        template = os.path.join('Habits', 'confirm_del.html')
        context = {
        }
        return render(request, template, context=context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = models.Habit.objects.get(pk=pk)
        obj.delete()
        messages.success(self.request, 'Task deleted...onto tougher tasks! ')
        return redirect('habit-list')




