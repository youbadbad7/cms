from rest_framework import serializers
from .models import Article


# 分类序列化
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'