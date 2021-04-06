from rest_framework import serializers
from categories.models import Category

# # 分类序列化
# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(label='ID', read_only=True)
#     name = serializers.CharField(label='名称', max_length=20)
#     sort = serializers.IntegerField(label='排序', required=False)
#     course_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 看这里
#
#     # 新增
#     def create(self, validated_data):
#         return Category.objects.create(**validated_data)
#
#     # 更新
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.sort = validated_data.get('sort', instance.sort)
#         instance.save()
#         return instance

# 分类序列化
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'