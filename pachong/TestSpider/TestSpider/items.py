# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestspiderItem(scrapy.Item):
    #新闻标题
    title = scrapy.Field()
    #链接地址
    url = scrapy.Field()
    #详情页的正文
    detail_content = scrapy.Field()
    #详情页的时间
    detail_time = scrapy.Field()
    #详情页的来源
    detail_resource = scrapy.Field()
    #详情页的图片地址
    detail_url = scrapy.Field()
