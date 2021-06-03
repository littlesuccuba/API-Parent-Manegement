from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User
from django.core.cache import cache

# 定义用户模型序列化器
class UserSerializer(ModelSerializer):
    # phone_num = serializers.CharField(required=True, max_length=11)
    # 序列化是否可登陆字段，用户注册时默认设置为可登陆
    is_active = serializers.BooleanField(default=True, required=False,help_text='用户是否可登陆')
    # 注册时密码加密方法重写
    def create(self, validated_data):
        # 将redis缓存中的手机号写入用户信息表
        validated_data['phone_num'] = cache.get('phone')
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # 创建用户成功后销毁redis缓存
        cache.set('phone', '', timeout=0)
        return user
    # 修改密码时密码加密重写
    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance = instance, validated_data = validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
            user.save()
            return user
        user.save()
        return user
    class Meta:
        model = User
        fields = '__all__'
        # 在API文档中显示的字段说明
        extra_kwargs = {
            'username': {
                'help_text': '用户名'
            },
            'password': {
                'help_text': '密码'
            },
            'last_login': {
                'help_text': '最后登录时间（不需要用户提供）'
            },
            'is_superuser': {
                'help_text': '是否为超级管理员'
            },
            'email': {
                'help_text': '邮箱（可选）'
            },
            'date_joined': {
                'help_text': '用户注册时间'
            },
            'name': {
                'help_text': '用户姓名（可选）'
            },
            'identity': {
                'help_text': '用户身份（可选，默认值为普通用户）'
            },
            'phone_num': {
                'help_text': '手机号码（必须）'
            }
        }