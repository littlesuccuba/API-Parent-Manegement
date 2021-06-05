from django.db import models


# Create your models here.

class Activity_Info(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=20)
    hour = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    new_price = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    hourTag = models.BooleanField
