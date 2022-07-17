import scrapy
from ..items import PaginationItem


class Pagination(scrapy.Spider):
    name = 'quotes'
    page_number=2
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
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
        items = PaginationItem()  # instance of a class
        all_div = response.css('div.quote')
        for quotes in all_div:  # to extract all data for each tuple one by one

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
            items['title'] = title  # should be same as item.py(objects)
            items['author'] = author
            items['tag'] = tag

            yield items  # scrapy crawl quotes -o items.csv|xml|json(in terminal)   to store data in any format csv,json and xml
        next_page ='http://quotes.toscrape.com/page/'+ str(Pagination.page_number) + '/'
        print(next_page)
        if Pagination.page_number <= 11:
            Pagination.page_number += 1
            yield response.follow(next_page, callback=self.parse)
