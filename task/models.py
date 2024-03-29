from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now) # auto_now_add=True
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + ' - ' + self.title + ' - ' + self.user.get_username()