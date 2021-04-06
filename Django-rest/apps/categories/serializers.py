from rest_framework import serializers
from .models import Category


# 分类序列化
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'