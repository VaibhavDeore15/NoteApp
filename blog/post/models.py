from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=100)
    msg=models.TextField(max_length=100)
    created_at=models.TimeField(auto_now=True)
    ispublish=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username