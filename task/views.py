from django.shortcuts import render, redirect
# from . import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "home.html",{
        # "form": UserCreationForm()
    })
    
def signup(request):
    if request.method == "POST":
        print('procesar', request.POST)
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
                                     password=request.POST['password1'])   
            user.save()
            return redirect('home')

    return render(request, "signup.html",{
        "form": UserCreationForm(),
        "error": "An error to be showed"
    })

