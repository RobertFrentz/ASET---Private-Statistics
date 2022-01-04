from django.urls import path
from .views import Users, Statistics, Patients, Hospitals
from .views import Login

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/login/', Login.as_view()),
    path('statistics/request/', Statistics.as_view()),
    path('patients/addPatients/', Patients.as_view()),
    path('hospitals/', Hospitals.as_view())
]
