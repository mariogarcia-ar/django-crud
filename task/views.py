from django.shortcuts import render
from . import forms 

# Create your views here.
def signup(request):
    return render(request, "signup.html",{
        "form": forms.SignUpForm()
    })

