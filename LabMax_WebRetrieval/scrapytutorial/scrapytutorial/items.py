# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapytutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 想要爬取的字段的信息为谚语内容, 作者, 标签
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
