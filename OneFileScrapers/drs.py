import scrapy
from scrapy.shell import inspect_response

class DrsSpider(scrapy.Spider):
    name = 'drs'
    url = ['https://drs.faa.gov/api/attivio/search/simpleSearch']
    start_urls= list(url)
    custom_settings = {
        'COOKIES_ENABLED':True,
        'COOKIES_DEBUG':True
    }

    def parse(self, response):
        inspect_response(response, self)
        request.headers.get('Cookie').split(b';')[-1].decode().strip().replace('jwt=','')

# request
#
# request.headers
#
# request.headers.get('Cookie')
#
# request.headers.get('Cookie').split(';')
#
# request.headers.get('Cookie').split(b';')[-1].decode().strip()
# #decode used for byte to str



