from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("signup/", views.signup , name="signup"),
    path("login/", views.login , name="login"),
    path("logout/", views.logout , name="logout"),

    path("tasks/", views.tasks , name="tasks"),
    path("create_task/", views.create_task , name="create_task"),
]
