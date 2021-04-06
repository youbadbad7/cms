from rest_framework import viewsets
from courses.models import Course
from admin.serializers.courses import CourseSerializer
from rest_framework.permissions import IsAdminUser


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]

