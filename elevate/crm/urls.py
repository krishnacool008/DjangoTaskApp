from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("", views.homepage, name=""),
    path("task", views.task, name="task"),
    path("createtask", views.createtask, name="createtask"),
    path("updatetask/<str:pk>", views.updatetask, name="updatetask"),
    path("deletetask/<str:pk>", views.deletetask, name="deletetask"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
]
