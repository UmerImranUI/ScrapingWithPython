import scrapy
from docx import Document
from htmldocx import HtmlToDocx
import scraper_helper


class GentenbergSpider(scrapy.Spider):
    name = 'gentenberg'
    # allowed_domains = ['x']
    start_urls = ['https://www.gutenberg.org/browse/scores/top#books-last30']

    def parse(self, response):
        css = 'ol:nth-child(18) li a:last-child ::attr(href)'
        links = response.css(css).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_book_summary)
            

    def parse_book_summary(self, response):
        xpath = '//a[contains(text(), "Read this book online") and contains(text(),"HTML")]/@href'
        url = response.xpath(xpath).get()
        if url:
            yield response.follow(url, callback=self.parse_book)

    def parse_book(self, response):
        document = Document()
        new_parser = HtmlToDocx()
        new_parser.options['images']=False    #ignore images
        book_title= response.xpath("//h1").xpath("normalize-space(.)").get()    #normalize to cleanup junk
        html = f"<h1>{book_title}</h1>"  #having html booktitle ias a header 
        html += ''.join(response.xpath(  # it waas returning a list so ''.join returns whole into html str
            '//h1/following-sibling::div[@class="chapter"]').getall())
        new_parser.add_html_to_document(html, document)   #appending the above html
        document.save(
            f'{book_title}.docx')    #saving 
        print(f'{book_title}.docx')   #prrint book title in the prog


scraper_helper.run_spider(GentenbergSpider)