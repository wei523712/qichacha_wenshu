# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WenshuItem(scrapy.Item):
    search_name = scrapy.Field()              #收索名
    name = scrapy.Field()                     #公司名
    number = scrapy.Field()                   #序号
    case_name = scrapy.Field()                #案件名称
    cause = scrapy.Field()                    #案由
    release_time = scrapy.Field()             #发布时间
    case_num = scrapy.Field()                 #案件编号
    case_status = scrapy.Field()              #案件身份
    executive_court = scrapy.Field()          #执行法院
    wsview = scrapy.Field()                   #文书的详细内容