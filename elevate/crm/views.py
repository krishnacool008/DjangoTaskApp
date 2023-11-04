from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import TaskForm, UserCreationForm, LoginForm
from .models import Task
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"RegisterForm": form}

    return render(request, "crm/register.html", context)


def homepage(request):
    return render(request, "crm/index.html")


def task(request):
    queryDataAll = Task.objects.all()
    context = {"AllTasks": queryDataAll}
    return render(request, "crm/task.html", context)


@login_required(login_url="login")
def createtask(request):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task")

    context = {"form": form}
    return render(request, "crm/createtask.html", context)


def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task")

    context = {"Updatedform": form}
    return render(request, "crm/updatetask.html", context)


def deletetask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task")

    return render(request, "crm/deletetask.html")


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {"LoginForm": form}
    return render(request, "crm/login.html", context)


@login_required(login_url="login")
def dashboard(request):
    return render(request, "crm/dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("")
