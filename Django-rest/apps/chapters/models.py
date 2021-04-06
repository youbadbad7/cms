from django.db import models
from courses.models import Course


# 章节
class Chapter(models.Model):
    CHOICES = (
        (0, '否'),
        (1, '是')
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')  # 外键
    title = models.CharField(max_length=50, verbose_name='标题')
    video = models.CharField(max_length=255, verbose_name='视频地址')
    time = models.IntegerField(default=0, verbose_name='时长')
    sort = models.IntegerField(default=0, verbose_name='排序')
    free = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='免费')
    published = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='发布')

    class Meta:
        db_table = 'chapters'  # 指明数据库表名
        verbose_name = '课程章节'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.title
