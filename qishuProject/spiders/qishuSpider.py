import scrapy


class QishuspiderSpider(scrapy.Spider):
    name = 'qishuSpider'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
