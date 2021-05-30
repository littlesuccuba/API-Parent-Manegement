from rest_framework.permissions import BasePermission   # 权限基类
from django.contrib.auth.models import Group

# 普通用户权限验证类
class IsOrdinaryUser(BasePermission):
    # 自定义返回信息
    message = '您没有权限！'
    def has_permission(self, request, view):
        # group为有权限的分组
        group = Group.objects.filter(id=1).first()
        # groups为当前用户所属的所有分组
        groups = request.user.groups.all()
        r2 = group and groups
        r3 = group in groups
        # 读接口大家都有权限，写接口必须为指定分组下的登陆用户
        return (r2 and r3)

# 管理员用户权限验证类
class IsAdminUser(BasePermission):
    # 自定义返回信息
    message = '您没有权限！'
    def has_permission(self, request, view):
        # group为有权限的分组
        group = Group.objects.filter(id=2).first()
        # groups为当前用户所属的所有分组
        groups = request.user.groups.all()
        r2 = group and groups
        r3 = group in groups
        # 读接口大家都有权限，写接口必须为指定分组下的登陆用户
        return (r2 and r3)