import datetime as dt
import pytest

from Habits.models import Habit
from UserProfile.models import Profile


'''The defined fixture functions that are to be used as data in testing.'''

'''The sample profile of an admin user.'''
@pytest.fixture()
def test_profile(admin_client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    user.save()
    profile = Profile.objects.get(user=user)
    profile.slug = 'John-Doe'
    profile.first_name = 'John'
    profile.second_name = 'test'
    profile.last_name = 'Doe'
    profile.date_run = '2024-10-10'
    profile.save()
    admin_client.force_login(user)

    return profile

'''The first 5 predefined habits of the sample profile.'''
@pytest.fixture()
def create_testhabit(test_profile):
    sample_run = Habit.objects.create(created = '2023-06-24 09:00:00+01:00', author = test_profile, name ='run', description ='2 hours', periodicity ='7')
    sample_swim = Habit.objects.create(created = '2023-06-24 09:00:00+01:00', author = test_profile, name ='swim', description ='2 hours', periodicity ='7')
    sample_cycle = Habit.objects.create(created = '2023-06-24 09:00:00+01:00', author = test_profile, name ='cycle', description ='3 hours', periodicity ='7')
    sample_sleep = Habit.objects.create(created = '2023-06-24 09:00:00+01:00', author = test_profile, name ='sleep', description ='8 hours', periodicity ='1')
    sample_coach = Habit.objects.create(created='2023-06-24 09:00:00+01:00', author=test_profile, name='Consult your coach', description='',
                                   periodicity='7')
    return sample_run, sample_swim, sample_cycle, sample_sleep,sample_coach


'''Dates when the habits were accomplished. This is used to test the analysis, consequently the current streak and maximum streak'''
@pytest.fixture()
def create_streak(create_testhabit):

    qs_h_run, qs_h_swim, qs_h_cycle, qs_h_sleep, qs_h_coach = create_testhabit


    now_list_run = [
        dt.datetime(2023, 6, 24, 9, 0, 0),
        dt.datetime(2023, 7, 1, 9, 0, 0),
        dt.datetime(2023, 7, 2, 9, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 7, 8, 9, 0, 0),
        dt.datetime(2023, 7, 16, 9, 0, 0), # more than periodicity, should reset streak
        dt.datetime(2023, 7, 23, 9, 0, 0)
    ]

    dict_run ={
        "Habit": qs_h_run,
        "datetime": now_list_run,
        "test_cur_streak": [1, 2, 2, 3, 1, 2],
        "test_max_streak": [1, 2, 2, 3, 3, 3],
    }

    now_list_swim = [
        dt.datetime(2023, 6, 25, 9, 0, 0),
        dt.datetime(2023, 7, 2, 6, 0, 0), # within the periodicity and just a few hours less , saves in tracker
        dt.datetime(2023, 7, 11, 10, 30, 0), # more than periodicity, should reset streak
        dt.datetime(2023, 7, 14, 14, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 7, 22, 9, 0, 0),  # more than periodicity, should reset streak
    ]
    dict_swim = {
        "Habit": qs_h_swim,
        "datetime": now_list_swim,
        "test_cur_streak": [1, 2, 1, 1, 1],
        "test_max_streak": [1, 2, 2, 2, 2],
    }

    now_list_cycle = [
        dt.datetime(2023, 6, 27, 17, 30, 0),
        dt.datetime(2023, 7, 4, 1, 0, 0),
        dt.datetime(2023, 7, 11, 10, 0, 0), # hours more than periodicity, should reset streak
        dt.datetime(2023, 7, 18, 23, 59, 59),
        dt.datetime(2023, 7, 26, 9, 0, 0) # more than periodicity, should reset streak
    ]
    dict_cycle = {
        "Habit": qs_h_cycle,
        "datetime": now_list_cycle,
        "test_cur_streak": [1, 2, 1, 2, 1],
        "test_max_streak": [1, 2, 2, 2, 2],
    }

    now_list_sleep = [
        dt.datetime(2023, 6, 24, 9, 0, 0),
        dt.datetime(2023, 6, 24, 22, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 6, 25, 9, 0, 0),
        dt.datetime(2023, 6, 25, 22, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 6, 26, 22, 0, 0),
        dt.datetime(2023, 6, 27, 22, 0, 0),
        dt.datetime(2023, 6, 28, 22, 0, 0),
        dt.datetime(2023, 6, 29, 22, 0, 0),
        dt.datetime(2023, 6, 30, 22, 0, 0),
        dt.datetime(2023, 7, 1, 22, 0, 0),
        dt.datetime(2023, 7, 2, 22, 0, 0),
        dt.datetime(2023, 7, 3, 22, 0, 0),
        dt.datetime(2023, 7, 4, 22, 0, 0),
        dt.datetime(2023, 7, 5, 20, 0, 0),
        dt.datetime(2023, 7, 6, 22, 0, 0),
        dt.datetime(2023, 7, 7, 22, 0, 0),
        dt.datetime(2023, 7, 9, 23, 0, 0), # more than periodicity, should reset streak
        dt.datetime(2023, 7, 10, 12, 0, 0),
        dt.datetime(2023, 7, 11, 12, 0, 0),
        dt.datetime(2023, 7, 12, 12, 0, 0),
        dt.datetime(2023, 7, 15, 21, 0, 0), # more than periodicity, should reset streak
        dt.datetime(2023, 7, 16, 21, 0, 0),
        dt.datetime(2023, 7, 17, 21, 0, 0),
        dt.datetime(2023, 7, 18, 21, 0, 0),
        dt.datetime(2023, 7, 19, 21, 0, 0),
        dt.datetime(2023, 7, 20, 21, 0, 0),
        dt.datetime(2023, 7, 21, 21, 0, 0),
        dt.datetime(2023, 7, 22, 21, 0, 0),
    ]
    dict_sleep = {
        "Habit": qs_h_sleep,
        "datetime": now_list_sleep,
        "test_cur_streak": [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8],
        "test_max_streak": [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    }

    now_list_coach = [
        dt.datetime(2023, 6, 25, 9, 0, 0),
        dt.datetime(2023, 6, 28, 9, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 6, 29, 9, 0, 0), # less than periodicity , should not save
        dt.datetime(2023, 7, 2, 9, 0, 0),
        dt.datetime(2023, 7, 15, 9, 0, 0), # more than periodicity, should reset streak
        dt.datetime(2023, 7, 22, 9, 0, 0)
    ]
    dict_coach = {
        "Habit": qs_h_coach,
        "datetime": now_list_coach,
        "test_cur_streak": [1, 1, 1, 2, 1, 2],
        "test_max_streak": [1, 1, 1, 2, 2, 2],
    }

    list_test = [
        dict_run,
        dict_swim,
        dict_cycle,
        dict_sleep,
        dict_coach
    ]
    return list_test
