from rest_framework import serializers
from .models import Course


# 分类序列化
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'