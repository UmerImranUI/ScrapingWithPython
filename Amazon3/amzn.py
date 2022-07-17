import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def start_requests(self):
        yield scrapy.Request(url="https://www.amazon.com/s?k=laptop")

    def parse(self, response):
        total_pages = response.xpath('//*[@class="a-pagination"]/li[last()-1]/text()').get()
        current_page =response.xpath('//*[@aria-current="page"]/text()').get()
       
        if total_pages and current_page:
            if int(current_page) ==1:   #without linkionk, by usin iteration you can optimize the code run time.
                for i in range(2, int(total_pages)+1):
                    url='https://www.amazon.com/s?k=laptop&page={}&qid=1656727951&ref=sr_pg_2'
                    yield response.Request(url.format(i))
                    
        for result in response.xpath('//*[@data-component-type="s-search-result"]'):
            name_xpath = './/*[@class="a-size-medium a-color-base a-text-normal"]/text()'
            product_title = result.xpath(name_xpath).get()
            price_dollar = result.xpath('.//*[@class="a-price-whole"]/text()').get()
            price_cents = result.xpath('.//*[@class="a-price-fraction"]/text()').get()

            item = dict()
            item['Product'] = product_title
            item['Price_Dollars'] = price_dollar
            item['Price_cents'] = price_cents

            yield item