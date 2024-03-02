from django.shortcuts import render
# from . import forms 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    return render(request, "signup.html",{
        "form": UserCreationForm()
    })

