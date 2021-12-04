from django.urls import path
import users.monitors.user_monitor
from .views import Users, Statistics
from .views import Login

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/login/', Login.as_view()),
    path('users/request/', Statistics.as_view())
]
