from pkg_resources import yield_lines
import scrapy

url='https://quotes.toscrape.com/api/quotes?page={}'
class ScrollSpider(scrapy.Spider):
    name = 'scrolly'
    start_urls = [url.format(1)]


    def parse(self, response):
        data=response.json()
        print(data["has_next"])
        print(data['page'])

        for quote in data["quotes"]:
            yield{
                'Author': quote["author"]["name"],
                'Quote':quote["text"]
            }

        current_page=data["page"]
        if data["has_next"]:
            next_page_url = url.format(current_page+1)
            yield scrapy.Request(next_page_url)
            
        

