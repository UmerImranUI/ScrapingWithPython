import scrapy
from scrapy import FormRequest

from ..items import LogInItem
# from scrapy.utils.response import open_in_browser

class LogIn(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()   #gets csrf value
        print(token)
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username': 'attreya01@gmail.com',
            'password' : 'dsadsdsa'
        },callback = self.start_scraping)

    def start_scraping(self,response):
        # open_in_browser(response)
        items = LogInItem()  # instance of a class
        all_div = response.css('div.quote')
        for quotes in all_div:  # to extract all data for each tuple one by one

            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
            items['title'] = title  # should be same as item.py(objects)
            items['author'] = author
            items['tag'] = tag

            yield items  # scrapy crawl quotes -o items.csv|xml|json(in terminal)   to store data in any format csv,json and xml



