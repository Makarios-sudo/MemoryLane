

from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [ 
    
    path('login', views.userLogin, name="userLogin"),
    path("registration", views.userRegistration, name="userRegistration"),
    path("logout", views.userLogout, name="userLogout"),

    path("profile/", views.profile, name="profile"),
    path("updateprofile/<str:pk>/", views.updateProfile, name="update")
]