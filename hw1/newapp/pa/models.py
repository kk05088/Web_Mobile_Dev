from django.db import models

# Create your models here.
def User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def Project(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)