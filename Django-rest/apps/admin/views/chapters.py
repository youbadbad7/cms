from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from chapters.models import Chapter
from admin.serializers.chapters import ChapterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    # permission_classes = [IsAuthenticated]

    # def get_serializer(self, *args, **kwargs):
    #     if 'data' in kwargs:
    #         data = kwargs['data']
    #         if isinstance(data, list):
    #             kwargs['many'] = True
    #
    #     return super(ChapterViewSet, self).get_serializer(*args, **kwargs)

class ChapterHomeView(APIView):
    def get(self,request,id):
        # return HttpResponse('123')
        chapters = Chapter.objects.filter(course_id=id)
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)