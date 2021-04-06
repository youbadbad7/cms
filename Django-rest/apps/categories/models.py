from django.db import models


# 定义分类
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    sort = models.IntegerField(default=0, verbose_name='排序')

    class Meta:
        db_table = 'categories'  # 指明数据库表名
        verbose_name = '视频分类'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name