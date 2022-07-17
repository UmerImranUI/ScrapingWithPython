import scrapy


class AwsImg(scrapy.Spider):
    name = 'aws'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        images=list()
        for img in response.css('.thumbnail::attr(src)').getall():
            images.append(response.urljoin(img))

        yield {
            'image_urls':images
        }