# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    av_num = scrapy.Field()
    author= scrapy.Field()
    play_num = scrapy.Field()
    bullet_screen = scrapy.Field()
    like = scrapy.Field()
    coin = scrapy.Field()
    collect = scrapy.Field()
    subscriber = scrapy.Field()
    pass
