from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Chapter
from courses.models import Course
from .serializers import ChapterSerializer
from courses.serializers import CourseSerializer
from rest_framework.response import Response


class ChapterDetailView(APIView):
    def get(self, request, chapter_id):

        # 当前章节
        chapter = Chapter.objects.get(id=chapter_id)
        chapter_serializer = ChapterSerializer(chapter)

        # 章节对应课程
        courser_serializer = CourseSerializer(chapter.course)

        # 当前课程全部章节
        chapters = Chapter.objects.filter(course_id=chapter.course_id)
        chapters_serializer = ChapterSerializer(chapters, many=True)

        return Response({'chapter': chapter_serializer.data,
                         'course': courser_serializer.data,
                         'chapters': chapters_serializer.data
                         })
