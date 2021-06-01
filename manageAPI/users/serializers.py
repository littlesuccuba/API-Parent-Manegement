from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User
from django.core.cache import cache

# 定义用户模型序列化器
class UserSerializer(ModelSerializer):
    # 序列化是否可登陆字段，用户注册时默认设置为可登陆
    is_active = serializers.BooleanField(default=True, required=False,help_text='用户是否可登陆', label='是否允许登陆')
    def create(self, validated_data):
        # 将redis缓存中的手机号写入用户信息表
        validated_data['phone_num'] = cache.get('phone')
        # 如果有is_staff属性则为管理员用户，否则为普通用户
        if validated_data['is_staff']:
            # 分配至管理员用户组
            validated_data['groups'] = [2]
        else:
            # 分配至普通用户组
            validated_data['groups'] = [1]
        # 注册时密码加密方法重写
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
        fields = ['id', 'username','phone_num', 'password', 'email', 'name', 'identity', 'is_active','is_staff', 'groups', 'user_permissions']
        # fields = '__all__'
        # 在API文档中显示的字段说明
        extra_kwargs = {
            'username': {
                'help_text': '用户名'
            },
            'password': {
                'help_text': '密码',
                'label': '密码',
                'write_only': True
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
                'label': '昵称',
                'help_text': '用户姓名（可选）'
            },
            'identity': {
                'label': '用户身份',
                'help_text': '用户身份（可选，默认值为普通用户）'
            },
            'phone_num': {
                'label': '手机号',
                'help_text': '手机号码（必须）'
            },
            'is_staff': {
                'write_only': True
            },
            'user_permissions': {
                'label': '用户权限',
                'help_text': '用户所拥有的权限（默认为空）',
                'write_only': True
            },
            'user_permissions': {
                'label': '用户组',
                'help_text': '用户所在用户组，该组拥有一定权限（默认普通用户）',
                'write_only': True
            }
        }