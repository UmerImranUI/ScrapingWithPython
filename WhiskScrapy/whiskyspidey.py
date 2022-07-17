
from gc import callbacks
import scrapy
class WhiskeySpidey(scrapy.Spider):
    name='spidey'
    start_urls='https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock'

    def parse(self, response):
        for products in response.css('.product-item-info'):
            try:
                yield{
                    'name':products.css('.product-item-link::text').get(),
                    'price':products.css('.price::text').get(),
                    'link':products.css('a.product-item-link').attrib['href']
                }
            except:
                yield{
                    'name':products.css('.product-item-link::text').get(),
                    'price':'sold out',
                    'link':products.css('a.product-item-link').attrib['href']
                }
        next_page=response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

                