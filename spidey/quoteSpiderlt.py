
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # def parse(self, response):
    # all_div=response.css('div.quote')   //to extract all data
    # title=all_div.css("span.text::text").extract()
    # author=all_div.css(".author::text").extract()
    # tag=all_div.css(".tag::text").extract()

    # yield{
    #     'title': title,
    #     'author':author,
    #     'tag':tag
    # }
    def parse(self, response):
        all_div = response.css('div.quote')
        for quotes in all_div:     # to extract all data for each tuple one by one
            
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            yield{
            'title': title,
            'author': author,
            'tag': tag
            }

                        

