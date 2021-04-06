from rest_framework.views import APIView
from .models import Category
from courses.models import Course
from .serializers import CategorySerializer
from courses.serializers import CourseSerializer
from rest_framework.response import Response


class ListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories':serializer.data})

class CourseListView(APIView):
    def get(self, request,category_id):
        courses = Course.objects.filter(category_id=category_id)
        serializer = CourseSerializer(courses, many=True)
        return Response({'courses':serializer.data})