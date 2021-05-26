from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [

]
# 创建路由器

child_router = DefaultRouter()
course_router = DefaultRouter()
course_Class_router = DefaultRouter()
child_Course_Grades_router = DefaultRouter()
classInfo_router = DefaultRouter()
classInfo_router.register(r'^class', views.ClassInfoViewSet)
# 注册路由器

child_router.register(r'^child', views.ChildViewSet)
course_router.register(r'^course', views.CourseViewSet)
course_Class_router.register(r'course_class', views.Course_ClassViewSet)
child_Course_Grades_router.register(r'grades', views.Child_Course_GradesViewSet)
urlpatterns += child_router.urls + course_router.urls + course_Class_router.urls + child_Course_Grades_router.urls + classInfo_router.urls   # 把生成好的路由拼接到urlpatterns
