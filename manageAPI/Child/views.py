from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Child_Info, Course, Course_Class, Child_Course_Grades, Class_Info
from .serializers import ChildInfoModelSerializer, CourseModelSerializer, Course_ClassModelSerializer, Child_Course_GradesModelSerializer, Class_InfoModelSerializer


class ChildViewSet(ModelViewSet):
    queryset = Child_Info.objects.all()
    serializer_class = ChildInfoModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class ClassInfoViewSet(ModelViewSet):
    queryset = Class_Info.objects.all()
    serializer_class = Class_InfoModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class Course_ClassViewSet(ModelViewSet):
    queryset = Course_Class.objects.all()
    serializer_class = Course_ClassModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


class Child_Course_GradesViewSet(ModelViewSet):
    queryset = Child_Course_Grades.objects.all()
    serializer_class = Child_Course_GradesModelSerializer
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]


