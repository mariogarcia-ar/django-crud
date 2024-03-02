from django import forms
from .models import Task 

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateTaskForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)

# create a Form using Models
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  
        fields = ['title', 'description', 'important']