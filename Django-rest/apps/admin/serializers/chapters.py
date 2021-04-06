from rest_framework import serializers
from chapters.models import Chapter
from admin.serializers.courses import CourseSerializer

# 分类序列化
class ChapterSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    class Meta:
        model = Chapter
        fields = '__all__'