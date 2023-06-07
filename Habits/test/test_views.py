from django import urls
import pytest
from django.utils.timezone import make_aware
import pytz

from Habits.models import Habit
from Habits.analysis import analyse

'''Tests whether the 5 predefined habits are saved in the Habit model '''
@pytest.mark.django_db
def test_habit_save(admin_client, create_testhabit):
    habit_model = Habit.objects.all()
    assert habit_model.count() == 5

'''Tests whether the trackers are added and the streak attribute is updated by the analysis'''
@pytest.mark.django_db
def test_tracker_save(admin_client, create_streak):
    list_test = create_streak
    for i_habit in range(0,len(list_test)):
        qs_h =  list_test[i_habit]["Habit"]
        now_list = list_test[i_habit]["datetime"]
        test_list_cur =  list_test[i_habit]["test_cur_streak"]
        test_list_max = list_test[i_habit]["test_max_streak"]
        for i_now in range(0,len(now_list)):
            aware = make_aware(now_list[i_now], timezone=pytz.timezone("Europe/Berlin"))
            streak, flag, condition = analyse(qs_h, aware)
            assert qs_h.cur_streak() == test_list_cur[i_now]
            assert qs_h.max_streak() == test_list_max[i_now]

'''Tests the view when a habit is shown or tallied'''
def test_redir_habit_view(admin_client):
    temp_url = urls.reverse('habit-list')
    resp = admin_client.get(temp_url)
    assert resp.status_code == 200

'''Tests for redirection when a habit is deleted'''
def test_redir_delete_view(admin_client):
    temp_url = urls.reverse('habit-delete', kwargs={'pk':Habit.pk})
    resp = admin_client.get(temp_url)
    assert resp.status_code == 200
