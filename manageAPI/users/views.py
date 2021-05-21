from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import User
from users.sms import SendSms


# 获取短信验证码
class send(View):
    def get(self,request):
        phone = request.GET.get('phone')
        code = SendSms.Send(phone)
        if code.SendStatusSet[0].Code == 'Ok':
            res = code.to_json_string(indent=2)
            return HttpResponse(res)



# 用户表增删改查(已包括用户注册)
class UserViewset(ModelViewSet):
    # 登录接口无需权限与认证
    authentication_classes = []
    permission_classes = []
    # 指定查询集
    queryset = User.objects.all()
    # 指定序列化器
    serializer_class = UserSerializer

    '''
    list:
    返回所有项目信息
    
    create:
    创建项目

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