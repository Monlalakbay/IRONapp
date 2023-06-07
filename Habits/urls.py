from django.urls import path

from . import views

'''The mapping between the URL path expression to the views. '''

urlpatterns = [
    path(' ',views.habit_list_view.as_view(), name='habit-list'),
    path('habit/<pk>/delete', views.habit_delete_view.as_view(), name='habit-delete'),
]

