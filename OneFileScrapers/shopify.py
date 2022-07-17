import math
import scrapy

#find api or disable javascript and click nec=xt link
class ShopifySpider(scrapy.Spider):
    name = 'spidey'
    start_urls = ['https://techinstr.myshopify.com/collections/all']

    def parse(self, response):
        raw = response.css('.filters-toolbar__product-count::text').get()
        total_cnt = int(raw.replace('products', ''))
        total_pages = math.ceil(total_cnt/8)

        

        yield{
            'products': response.css('.grid-view-item__link > span ::text').getall()
        }

        for i in range(2,total_pages+1):
            url = 'https://techinstr.myshopify.com/collections/all?page='.format(i)
            yield scrapy.Request(url, callback=self.parse_api)


        

    def parse_api(self, response):
        yield{
            'products': response.css('.grid-view-item__link > span ::text').getall()
        }

