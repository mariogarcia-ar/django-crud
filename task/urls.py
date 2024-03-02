from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("signup/", views.signup , name="signup"),
    path("login/", views.signin , name="login"),
    path("logout/", views.signout , name="logout"),

    path("tasks/", views.tasks , name="tasks"),
    path("create_task/", views.create_task , name="create_task"),
    path("task/<int:id>/", views.detail_task , name="detail_task"),
]
