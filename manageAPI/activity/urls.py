from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = []

Activity_router = DefaultRouter()
Activity_router.register(r'^activity', views.ActivityViewSet)
urlpatterns += Activity_router.urls
