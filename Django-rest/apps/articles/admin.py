from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content','img_url','thumb_image']


admin.site.register(Article,ArticleAdmin)




