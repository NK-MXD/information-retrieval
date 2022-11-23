import scrapy


class InfoSpider(scrapy.Spider):
    name = 'info'
    allowed_domains = ['www.nankai.edu.cn']
    start_urls = ['http://www.nankai.edu.cn/']

    def parse(self, response):
        pass
