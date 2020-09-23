# !/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy
import time
from scrapy_splash import SplashRequest
import re

from bilibili.items import BilibiliItem
#
# logging.basicConfig(filename="test.log", level=logging.INFO,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class BILIBILI(scrapy.Spider):
    name = 'bilibili'
    start_urls = ['https://www.bilibili.com/v/digital/mobile/?spm_id_from=333.68.b_7072696d6172795f6d656e75.55#/']
    allowed_domains = ['bilibili.com']
    av_num = 0

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'images': 0, 'timeout': 5,'wait':0.5})

    def parse(self, response):
        # print(response.text)
        post_nodes = response.css(".vd-list-cnt li .l-item .l .spread-module a::attr(href)").extract()
        for post_url in post_nodes:
            # print(post_url)
        #
        # for post_node in post_nodes:

        #     post_url = post_node.css(".l-item .r a::attr(href)").extract_first("")
        #     # av_num = post_url

            # self.av_num = post_url

            yield SplashRequest(url='https://www.bilibili.com'+post_url, callback=self.parse_data,dont_filter=False)

        # next_url = response.css(".page-item next .nav-btn iconfont icon-arrowdown3").extract_first("")
        # if next_url:
        #     logging.info('start parsing {}'.format(next_url))
        #
        #     yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=False)

    def parse_data(self, response):
        # print(response.text)
        get_data = lambda x: re.findall("\d+",response.xpath(x)[0].attrib.get('title'))[0] if len(re.findall("\d+",response.xpath(x)[0].attrib.get('title'))) != 0 else 0
        get_subscriber = lambda x: response.xpath(x).extract()[0] if len(response.xpath(x).extract()) != 0 else 0
        item = BilibiliItem()
        item['title'] = str(response.xpath('''//*[@id="viewbox_report"]/h1/span/text()''').extract()[0]).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['play_num'] = str(get_data('''//*[@id="viewbox_report"]/div[2]/span[1]''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['bullet_screen'] = str(get_data('''//*[@id="viewbox_report"]/div[2]/span[2]''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        # item['like'] = response.xpath('''//*[@id="arc_toolbar_report"]/div[1]/span[1]/text()''')
        item['like'] = str(get_data('''//*[@id="arc_toolbar_report"]/div[1]/span[1]''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['coin'] = str(get_subscriber('''//*[@id="arc_toolbar_report"]/div[1]/span[2]/text()''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['collect'] =  str(get_subscriber('''//*[@id="arc_toolbar_report"]/div[1]/span[3]/text()''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        # item['subscriber'] = response.xpath('''//*[@id="v_upinfo"]/div[3]/div[2]/span/span/text()''').extract()[0]
        item['subscriber'] = str(get_subscriber('''//*[@id="v_upinfo"]/div[3]/div[2]/span/span/text()''')).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['author'] = str(response.xpath('''//*[@id="v_upinfo"]/div[2]/div/a[1]/text()''').extract()[0]).replace("-","").replace(r"\n","").replace("\n","").replace(" ","")
        item['av_num'] = 0

        return item
#     name = 'bilibili'
#
#     allowed_domains = ['bilibili.com']
#     start_urls = ['https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90']
#
#
# # def start_requests(self):
# #     yield SplashRequest('https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90', args={'wait': 0.5})
#
#
#     def parse(self, response):

#         print(response.text)
