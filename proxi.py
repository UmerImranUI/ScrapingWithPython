
import scrapy
from ..items import ProxibypsItem


class Proxibyps(scrapy.Spider):
    name = 'amazon'
    start_urls=[
        "https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1655525986&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"
    ]

    def parse(self, response):
        items = ProxibypsItem()
        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.s-link-style').css('::text').extract()
        product_price = response.css(
            '.s-price-instructions-style .a-price-fraction , .s-price-instructions-style .a-price-whole').css(
            '::text').extract()
        product_img = response.css('.s-image').css('::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_img'] = product_img

        yield items