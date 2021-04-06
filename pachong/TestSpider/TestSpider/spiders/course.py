# -*- coding: utf-8 -*-
import scrapy
from TestSpider.items import TestspiderItem

class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['http://finance.eastmoney.com']
    start_urls = ['http://finance.eastmoney.com/a/cgnjj.html']

    def parse(self, response):
        for course in response.xpath('//div[@id="repeatList"]/div/a'):
            item = TestspiderItem()
