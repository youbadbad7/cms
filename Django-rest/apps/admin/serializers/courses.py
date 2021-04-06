from rest_framework import serializers
from courses.models import Course
from admin.serializers.category import CategorySerializer



# 分类序列化
class CourseSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Course
        fields = '__all__'
