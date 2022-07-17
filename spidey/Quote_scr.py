import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('.quote:nth-child(3) .text::text , .quote:nth-child(1) .text::text').extract()
        yield {'titleText': title}