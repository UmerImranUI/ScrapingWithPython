from spidey.items import Article
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ArticleSpider(CrawlSpider):
    name="article"
    allowed_domains=["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page", "https://en.wikipedia.org/wiki/Python_28%programming_language%29"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback ='parse_item', follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: "+title)
        item['title']=title
        return item