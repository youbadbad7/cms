from django.db import models
from categories.models import Category



# 课程
class Course(models.Model):
    CHOICES = (
        (0, '否'),
        (1, '是')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')  # 外键
    name = models.CharField(max_length=50, verbose_name='名称')
    url = models.CharField(max_length=255, verbose_name='图片地址',null=True)
    target_person = models.CharField(max_length=255, verbose_name='目标人群')
    target_person_details = models.TextField(max_length=255, verbose_name='目标人群详情')
    free = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='免费')
    published = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='发布')
    completed = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='完结')
    recommended = models.SmallIntegerField(choices=CHOICES, default=0, verbose_name='推荐')
    updated_at = models.DateField(auto_now=True,verbose_name='发布日期')

    class Meta:
        db_table = 'courses'  # 指明数据库表名
        verbose_name = '视频课程'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name