from django.db import models
from utils.common import MyStorage
from django.utils.safestring import mark_safe


# 定义分类
class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    img_url = models.ImageField(storage=MyStorage(),null=True, verbose_name='图片地址')
    sort = models.IntegerField(default=0, verbose_name='排序')


    class Meta:
        db_table = 'articles'  # 指明数据库表名
        verbose_name = '文章'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.title


    def thumb_image(self):
        if not self.img_url:
            return '无图片'
        else:
            return mark_safe(
                '<img src="%s" style="height: 60px; border-radius: 5px;">' % (self.img_url))

    thumb_image.short_description = '缩略图'
