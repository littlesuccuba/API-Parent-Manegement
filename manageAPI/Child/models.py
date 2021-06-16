from django.db import models
from .util import UploadFilesReName


# Create your models here.
# 创建孩子信息表
class Child_Info(models.Model):
    childID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    image = models.ImageField(max_length=255, upload_to=UploadFilesReName.rename, null=True)


# 创建班级信息表
class Class_Info(models.Model):
    # childID = models.ForeignKey(Child_Info, on_delete=models.CASCADE)
    classID = models.CharField(max_length=20, primary_key=True)
    # classID = models.ForeignKey(Class, on_delete=models.CASCADE)
    className = models.CharField(max_length=20, default='未命名')


# 创建课程表
class Course(models.Model):
    courseID = models.CharField(max_length=20, primary_key=True)
    courseName = models.CharField(max_length=20, unique=False)


# 创建班级课程表
class Course_Class(models.Model):
    classID = models.ForeignKey(Class_Info, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)


# 创建孩子课程成绩表
class Child_Course_Grades(models.Model):
    childID = models.ForeignKey(Child_Info, on_delete=models.CASCADE)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    grades = models.DecimalField(max_digits=5, decimal_places=2)
