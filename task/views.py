from django.shortcuts import render, redirect
# from . import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import models

# Create your views here.
def home(request):
    return render(request, "home.html",{
        # "form": UserCreationForm()
    })
    
def tasks(request):
    # tasks = models.Task.objects.all()
    tasks = models.Task.objects.filter(user=request.user)
    return render(request, "tasks.html",{
        "tasks": tasks
    })


def signup(request):
    if request.method == "POST":
        print('procesar', request.POST)
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                     password=request.POST['password1'])   
            user.save()
            
            # session login
            login(request, user)

            return redirect('tasks')

    return render(request, "signup.html",{
        "form": UserCreationForm(),
        "error": "An error to be showed"
    })

