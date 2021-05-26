from rest_framework import serializers

from .models import Child_Info, Course, Course_Class, Child_Course_Grades, Class_Info


class ChildInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Info
        fields = '__all__'


class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class Course_ClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Class
        fields = '__all__'


class Child_Course_GradesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child_Course_Grades
        fields = '__all__'


class Class_InfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Info
        fields = '__all__'
