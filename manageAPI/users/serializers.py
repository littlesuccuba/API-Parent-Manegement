from rest_framework.serializers import ModelSerializer
from users.models import User

# 定义用户模型序列化器
class UserSerializer(ModelSerializer):
    # 密码加密方法重写
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data['password'])
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
            'phone_num': {
                'help_text': '电话号码（必须）'
            },
            'name': {
                'help_text': '用户姓名（可选）'
            },
            'identity': {
                'help_text': '用户身份（可选，默认值为普通用户）'
            }
        }