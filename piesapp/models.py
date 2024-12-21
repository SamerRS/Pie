from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pie(models.Model):
    name = models.CharField(max_length=100)
    filling = models.CharField(max_length=100)
    crust = models.CharField(max_length=100)
    baker = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pie = models.ForeignKey(Pie, on_delete=models.CASCADE)

