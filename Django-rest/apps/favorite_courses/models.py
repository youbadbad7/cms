from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

# 用户喜欢的课程的中间表
class Favorite_course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='分类')  # 外键
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='分类')  # 外键


    class Meta:
        db_table = 'Favorite_courses'  # 指明数据库表名
        verbose_name = '用户课程中间表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.user