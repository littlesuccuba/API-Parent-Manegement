from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 重写用户表、需要继承 AbstractUser
class User(AbstractUser):
    phone_num = models.CharField(max_length=11, default='', null=False, blank=False, unique=True)
    name = models.CharField(max_length=30, default='未命名', unique=False)
    identity = models.CharField(choices=(
        ('1','普通用户'),
        ('2','管理员')
    ), default='1', max_length=255)

