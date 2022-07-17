import scrapy


class CraigslistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    hood = scrapy.Field()
    link = scrapy.Field()
    misc = scrapy.Field()
    lon = scrapy.Field()
    lat = scrapy.Field()