from django.db import models
from django.contrib.auth.models import AbstractUser
from users.util import UploadFilesReName
# Create your models here.

# 重写用户表、需要继承 AbstractUser
class User(AbstractUser):
    # 手机号字段
    phone_num = models.CharField(max_length=11, default='', null=False, blank=False, unique=True)
    # 昵称字段（可选）
    name = models.CharField(max_length=30, default='未命名', unique=False)
    # 用户身份
    identity = models.CharField(choices=(
        ('1','普通用户'),
        ('2','管理员')
    ), default='1', max_length=255)
    # 是否允许登陆
    is_active = models.BooleanField(default=True)
    # 用户头像地址
    avatar = models.ImageField(null=True, upload_to=UploadFilesReName.rename)


