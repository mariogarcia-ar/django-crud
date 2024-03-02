from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import forms 
from . import models

# Create your views here.
def home(request):
    return render(request, "home.html",{
        # "form": UserCreationForm()
    })
    
def signin(request):
    error = ""

    if request.method == "POST":
        print('procesar signin', request.POST)
        
        user = authenticate(request, username=request.POST['username'],
                                     password=request.POST['password'],)
        if user :
            login(request, user)
            return redirect('tasks')
        else:
            error = "User or Password Incorrect"
        
    return render(request, "login.html",{
        "form": AuthenticationForm(),
        "error": error
    })

def signout(request):
    logout(request)
    return redirect('home')
    
@login_required    
def tasks(request):
    # tasks = models.Task.objects.all()
    tasks = models.Task.objects.filter(user=request.user)
    return render(request, "tasks/tasks.html",{
        "tasks": tasks
    })

@login_required    
def create_task(request):
    if request.method == "POST":
        print('procesar create_task', request.POST)
        
        # task = models.Task.objects.create(title=request.POST['title'],
        #                                 description=request.POST['description'],
        #                                 user=request.user)
        # task.save()
        form = forms.TaskForm(request.POST)
        task = form.save(commit=False) # waiting for user
        task.user = request.user 
        task.save()

        return redirect('tasks')
            
    return render(request, "tasks/create_task.html",{
        "form": forms.TaskForm()
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

