from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from django.core.paginator import Paginator,Page



#新闻详情
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        paginator = Paginator(articles, 9)  # 实例化paginator，每页X条数据
        page_number = int(request.query_params.get('page'))  # 获取当前页码

        total_page = paginator.num_pages #总页数

        #是否有下一页
        has_next=page_number+1
        if has_next>total_page:
            has_next=False

        articles = paginator.get_page(page_number)
        chapters_serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': chapters_serializer.data,
                         'current_page':page_number,
                         'has_next':has_next
                         })
