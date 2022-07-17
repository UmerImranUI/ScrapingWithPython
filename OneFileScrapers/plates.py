
import scrapy
import pandas as pd

url='https://vplates.com.au/vplatesapi/checkcombo?vehicleType=car&combination={}'
class PlatesSpider(scrapy.Spider):
    name = 'plates'

    def start_requests(self):
        df = pd.read_csv('D:\py\Scrapy_up\input.csv')
        for word in df['search'].tolist():
            yield scrapy.Request(url.format(word), cb_kwargs={'lookup':word}) #sending word(key of Word) with url requests


    def parse(self, response,lookup):
        data = response.json() #bc response gettin is json
        success = data.get('success')

        yield{
            'search':lookup,
            'Available':'Yes' if success else 'No'
            }
