'''URL configuration for IRONapp project.'''

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',include('allauth.urls')),
    path('UserProfile/',include('UserProfile.urls')),
    path('Habit/',include('Habits.urls'))
]

handler404 = "helpers.views.handle_not_found"
handler500 = "helpers.views.handle_server_error"