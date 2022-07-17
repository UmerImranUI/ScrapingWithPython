# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class SqMyquotePipeline:

    def __init__(self):
        self.create_con()
        self.create_table()               #calls itself() instance

    def create_con(self):
        self.conn=mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Assasins123$',
            database = 'myquotes '
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(title text, author text, tag text)""")
        
    def process_item(self, item, spider):
        self.store_db(item)
        # print("Pipeline: "+item['title'][0])
        return item  #uncommment to access the pipeline.

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values(%s,%s,%s)""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()

