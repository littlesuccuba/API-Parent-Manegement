from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import User
from users.sms import SendSms
from django.core.cache import cache
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

# 导入自定义权限类
from .permission import IsAdminUser, IsOrdinaryUser

Users = get_user_model()
# 重写jwt认证接口
class CustomBackend(ModelBackend):
    # 手机号或用户名登陆
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 获取用户对象
        user = Users.objects.get(Q(username=username) | Q(phone_num=username))
        # 管理员登陆
        if user.is_staff:
            # 如果is_staff为True，则代表此用户为管理员
            try:
                # 尝试验证密码
                if user.check_password(password):
                    return user
            except Exception as e:
                return None
        # 普通用户登陆
        else:
            # 如果is_staff为False，则代表此用户为普通用户
            try:
                # 尝试验证密码
                if user.check_password(password):
                    return user
            except Exception as e:
                return None

# 获取短信验证码
class send(View):
    def get(self,request):
        phone = request.GET.get('phone')
        code = SendSms.Send(phone)
        if not cache.get('code') is None:
            return HttpResponse(status=200, content='发送成功')
        else:
            return HttpResponse(status=204, content='发送失败')


# 用户表增删改查(已包括用户注册)
class UserViewset(ModelViewSet):
    # 登录接口无需权限与认证
    authentication_classes = []
    permission_classes = []
    # 指定查询集
    queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer

    # 重写创建用户方法，先验证短信验证码正确才允许注册，否则返回403错误
    def create(self, request, *args, **kwargs):
        '''
        create:
        创建项目
        '''
        # 验证验证码结果：正确则注册，错误则返回异常
        if request.data.get('code') == cache.get('code'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            # 每次使用完验证码后必须销毁该验证码，防止恶意注册
            cache.set('code','', timeout=0)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'code': '403','message': '验证码验证失败'}, status=status.HTTP_403_FORBIDDEN)

    '''
    list:
    返回所有项目信息
    

    retrieve:
    获取某个项目的详细信息

    update:
    更新项目

    destroy：
    删除项目

    names:
    获取所有项目的名称

    interfaces:
    获取指定项目的所有接口信息
    '''