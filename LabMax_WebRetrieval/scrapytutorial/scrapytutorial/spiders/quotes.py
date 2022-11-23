import scrapy

class QuotesSpider(scrapy.Spider):
    # name用来区分的爬虫
    name = "quotes"
    # 允许爬取的域名范围
    allowed_domain = ["https://quotes.toscrape.com/"]
    # 初始请求列表
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # 对返回页面进行解析这里采用的解析方式为css解析器解析
        pass