from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    img = models.ImageField(upload_to='images/')
    text = models.TextField()
    text2 = models.IntegerField(null=True)
    text3 = models.IntegerField(null=True)

    def __str__(self):
        return self.text


class WorkmateUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name