from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog (models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    visible = models.BooleanField(default=False)
    imgfile = models.FileField()
