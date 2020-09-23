# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import sys

class BilibiliPipeline(object):
    def __init__(self):
        # sys.setdefaultencoding("utf-8")
        # logging.info('create json file')
        self.file = open('test.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)).encode('utf-8').decode('unicode-escape') + "\n"
        # line = json.dumps(dict(item)) + "\n"
        self.file.write(line.encode('utf-8'))


        return item

