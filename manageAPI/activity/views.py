from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Activity_Info
from .serializers import Activity_InfoModelSerializer


# Create your views here.
class ActivityViewSet(ModelViewSet):
    queryset = Activity_Info.objects.all()
    serializer_class = Activity_InfoModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
