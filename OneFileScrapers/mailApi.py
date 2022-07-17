import scrapy
from scrapy.crawler import CrawlerProcess
import config


class DetailsSpider(scrapy.Spider):
    name = 'details'
    start_urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']

    custom_settings = {
        'FEEDS': {
            'books.csv': {
                'format': 'csv'
            }
        }
    }

    def parse(self, response):
        for book_link in response.css('.product_pod h3 a::attr(href)').getall():
            yield scrapy.Request(response.urljoin(book_link), self.parse_book, )

    def parse_book(self, response):
        yield {
            'name': response.css('h1::text').get(),
            'price': response.css('.price_color::text').get().strip('£')
        }


def send_mail():
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg['From'] = config.EMAIL_USER
    msg['To'] = config.EMAIL_USER
    msg["Subject"] = "YOUTUBE ROCKS"
    msg.set_content("This is the message body")
    with open('books.csv', 'r') as f:
        data = f.read()
    msg.add_attachment(data, filename="books.csv")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    server.login(config.EMAIL_USER, config.EMAIL_PASS)
    server.send_message(msg)
    server.quit()


process = CrawlerProcess()
process.crawl(DetailsSpider)
process.start()
send_mail()