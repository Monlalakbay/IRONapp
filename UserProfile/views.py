from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

from UserProfile import models, forms

import os

'''The html response to the user registering and logging in.'''

def initial_data():
    dict_initial_data = {

    }
    return dict_initial_data

