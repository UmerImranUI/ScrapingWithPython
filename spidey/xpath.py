import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('.quote:nth-child(3) .text::text , .quote:nth-child(1) .text::text').extract()
        yield {'titleText': title}
#response.css("a").xpath("@href").extract()
#response.css("li.next a").xpath("@href").extract()
#response.xpath("//span[@class='text']/text()")[1].extract()
#response.css("a").xpath("@href").extract()
#response.xpath("//title/text()").extract()
#response.xpath("//title").extract()
