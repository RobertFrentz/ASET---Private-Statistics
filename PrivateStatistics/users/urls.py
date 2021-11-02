from django.urls import path

from .views import Users
from .views import Login

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/login/', Login.as_view()),
]
