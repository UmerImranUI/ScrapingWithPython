import scrapy
from ..items import NxtpgItem


class Nxtpg(scrapy.Spider):
    name = 'quotes'
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
        items = NxtpgItem()  # instance of a class
        all_div = response.css('div.quote')
        for quotes in all_div:  # to extract all data for each tuple one by one

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
            items['title'] = title  # should be same as item.py(objects)
            items['author'] = author
            items['tag'] = tag

            yield items  # scrapy crawl quotes -o items.csv|xml|json(in terminal)   to store data in any format csv,json and xml
        next_page=response.css('li.next a::attr(href)').get()       #to get next page
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)