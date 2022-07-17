import scrapy
from ..items import AmazoncrwlItem


class Amazoncrwl(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        "https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=1&qid=1655636584&rnid=1250225011&ref=sr_pg_2"
    ]

    def parse(self, response):
        items = AmazoncrwlItem()
        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_price = response.css(
            '.s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole').css(
            '::text').extract()
        product_img = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_img'] = product_img

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(
            Amazoncrwl.page_number) + '&qid=1655636584&rnid=1250225011&ref=sr_pg_2'
        if Amazoncrwl.page_number <= 5:
            Amazoncrwl.page_number += 1
            yield response.follow(next_page, callback=self.parse)
