from rest_framework import serializers
from .models import Activity_Info


class Activity_InfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_Info
        fields = '__all__'
