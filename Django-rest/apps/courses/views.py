from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Course
from chapters.models import Chapter
from .serializers import CourseSerializer
from chapters.serializers import ChapterSerializer
from rest_framework.response import Response
from django.utils import timezone


#课程详情
class DetailView(APIView):
    def get(self, request,course_id):
        #当前课程
        course = Course.objects.get(id=course_id)
        course_serializer = CourseSerializer(course)

        #当前课程对应的全部章节
        chapters = Chapter.objects.filter(course_id=course_id)
        chapters_serializer = ChapterSerializer(chapters, many=True)
        return Response({'course':course_serializer.data,'chapters':chapters_serializer.data})

#首页
class HomeView(APIView):
    def get(self, request):
        #推荐的课程
        recommended_courses =Course.objects.filter(recommended=True)
        recommended_serializer = CourseSerializer(recommended_courses,many=True)

        #课程日历
        calendar_courses = Course.objects.order_by('-updated_at')
        calendar_serializer = CourseSerializer(calendar_courses, many=True)

        return Response({'recommended_courses':recommended_serializer.data,
                         'calendar_courses':calendar_serializer.data})


#搜索
class SearchView(APIView):
    def get(self, request):
        name = request.query_params.get('q')
        search_name = Course.objects.filter(name__contains=name)
        search_serializer = CourseSerializer(search_name, many=True)

        return Response({'courses':search_serializer.data})




#课程日历
class CalendarView(APIView):
    def get(self, request):
        calendar_courses = Course.objects.order_by('-updated_at')
        calendar_serializer = CourseSerializer(calendar_courses, many=True)
        return Response({'calendar_courses': calendar_serializer.data})
