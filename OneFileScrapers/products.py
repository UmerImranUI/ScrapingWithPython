import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
