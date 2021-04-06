from django.contrib import admin
from django.urls import path, include
from admin.views.category import CategoryViewSet
from admin.views.courses import CourseViewSet
from admin.views.chapters import ChapterViewSet
from admin.views.articles import ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from admin.views import articles
from admin.views import chapters

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    # path('categories/', include('categories.urls')),
    path('', include(router.urls)),
    path('photo/', articles.ListView.as_view(), name='list'),
    path('chapter/<int:id>/', chapters.ChapterHomeView.as_view(), name='list'),

]
