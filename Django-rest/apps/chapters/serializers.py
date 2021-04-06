from rest_framework import serializers
from .models import Chapter


# 分类序列化
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'