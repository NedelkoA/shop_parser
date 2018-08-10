# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import os
import django
from scrapy.utils.serialize import ScrapyJSONEncoder


encoder = ScrapyJSONEncoder()

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))),
    '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'parser_django.settings'
django.setup()


class MyScrapyPipeline(object):
    def process_item(self, item, spider):
        from breuninger_shop.tasks import added_item
        added_item.delay(encoder.encode(item))
        return item
