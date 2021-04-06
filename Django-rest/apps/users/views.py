from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from chapters.models import Chapter
from users.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from favorite_courses.models import Favorite_course
from courses.models import Course
from courses.serializers import CourseSerializer
import re
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

#当前用户
class UserView(APIView):
    def get(self, request):
        id = request.user.id
        user = User.objects.get(id=id)
        user_serializers = UserSerializer(user)
        return Response({'user':user_serializers.data})

#当前用户收藏的课程
class User_favoriteView(APIView):
    def get(self, request):
        user_id = request.user.id
        favorite_courses_id = Favorite_course.objects.filter(user_id=user_id)
        courses = Course.objects.filter(id__in=list(favorite_courses_id.values_list('course_id',flat=True)))
        # print(list(favorite_courses_id.values_list('course_id',flat=True)))
        courses_serializers = CourseSerializer(courses,many=True)
        return Response({'favorite': courses_serializers.data})

#注册用户
class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not re.match('^[a-zA-Z0-9_-]{5,20}$', username):
            return JsonResponse({'status': False, 'msg': '用户名为5-20个字符'})

        if User.objects.filter(username=username).count() > 0:
            return JsonResponse({'status': False, 'msg': '用户名已经存在'})

        if not re.match('^[0-9A-Za-z]{6,20}$', password):
            return JsonResponse({'status': False, 'msg': '密码为6-20个字符'})

        # 创建用户
        User.objects.create_user(
            username=username,
            password=password,
            email=email,

        )



        return JsonResponse({'status': True, 'msg': '注册成功'})

class CustomBackend(ModelBackend):
    """邮箱也能登录"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None






