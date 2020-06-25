# -*- coding: utf-8 -*-
import scrapy


class A10xSpider(scrapy.Spider):
    # 三个默认属性
    name = '10x' # 爬虫名字唯一
    allowed_domains = ['www.10xgenomics.com/resources/publications']
    start_urls = ['http://www.10xgenomics.com/resources/publications']

    def parse(self, response):
       r = response.xpath("//div[@class='Block']/ul")
       for i in r:
         
