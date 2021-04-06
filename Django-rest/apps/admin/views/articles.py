from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article
from admin.serializers.articles import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from utils.common import Qiniu,MyStorage
from django.conf import settings
import uuid
import qiniu
import io
from PIL import Image


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticated]


def upload(file_name,file_read):
    q = qiniu.Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)
    key = file_name
    path = file_read
    token = q.upload_token(settings.QINIU_BUCKET_NAME, key, 3600, )
    qiniu.put_data(token, key, path)
    url = 'http://qfpa93ogx.hd-bkt.clouddn.com/{}'.format(key)
    return url

class ListView(APIView):
    def get(self,request):
        return HttpResponse('123')
    def post(self, request):
        file = request.FILES['file']
        file_name=file.name
        file_read=file.read()
        url = upload(file_name,file_read)

        # return HttpResponse(url)
        return JsonResponse({'status': True, 'msg': '新增成功','url':url})


        # return Response(
        #     {
        #         "name": name,
        #         # "file": file,
        #     }
        # )





