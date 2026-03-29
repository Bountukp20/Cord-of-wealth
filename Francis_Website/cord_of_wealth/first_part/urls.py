from django.urls import path
from .views import (
    home,
    store,
    login,
    signup,
)
from . import views

# app_name = 'first_part'

urlpatterns = [
    path("", home, name="home"),
    path("store", store, name="store"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
]
