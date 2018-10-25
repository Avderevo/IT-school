from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MyUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
