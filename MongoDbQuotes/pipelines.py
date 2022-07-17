# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo



class MonquotesPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017  # connects db
        )
        db = self.conn['myquotes']  # creates db
        self.collection = db['quotes_tb']

    def process_item(self, item, spider):
        self.collection.insert_many((item))
        return item
