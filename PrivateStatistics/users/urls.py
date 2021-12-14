from django.urls import path
from .views import Users, Statistics
from .views import Login

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/login/', Login.as_view()),
    path('statistics/request/', Statistics.as_view())
]
