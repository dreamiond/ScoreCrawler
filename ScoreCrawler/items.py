# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScorecrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    univName = scrapy.Field() # 院校名称
    positon = scrapy.Field() # 考生所在地
    category = scrapy.Field() # 考生类别
    batch = scrapy.Field() # 批次
    year = scrapy.Field() # 年份
    highestScore = scrapy.Field() # 最高分
    averageScore = scrapy.Field() # 平均分
