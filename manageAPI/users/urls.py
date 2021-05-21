from django.urls import path
from users import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register('user', views.UserViewset)

urlpatterns = [
    # jwt 登录视图，使用jwt自动签发token
    path('login/', obtain_jwt_token),
    # 短信验证码接口
    path('getnum/', views.send.as_view()),
]

urlpatterns += router.urls