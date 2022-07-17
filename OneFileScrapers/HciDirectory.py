from tkinter import Y
import scrapy


class HcidirectorySpider(scrapy.Spider):
    name = 'HciDirectory'
    start_urls = ['https://www.hcidirectory.gov.sg/hcidirectory/']

    def parse(self, response):
        data = {  # providing formdata for post form
            'RadioGroup1': 'HCI Name',
            'name': '',
            'clinicType': 'all'
        }
        # for the post request getting form
        yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_page)

    def parse_page(self, response):
        for result in response.xpath('//*[@class="result_container"]'):
            item = {
                'Name': result.css('.name a::text').get(),
                'phone': result.xpath('normalize-space(.//*[@class="tel"])').get(),
                'Address': result.xpath('normalize-space(.//*[@class="add"])').get(),
                'Time': result.xpath('normalize-space(.//*[@class="time"])').get(),

            }
            item['phone'] = item['phone'].replace('\xa0', ' ')
            yield item

        # pagination
        total_pages = response.css('#totalPage::attr(value)').get()
        current_page = response.css('#targetPageNo::attr(value)').get()

        if int(current_page) < 3:
        # if int(current_page)<int(total_pages):
            data = {
                'RadioGroup1': 'HCI Name',
                'name': '',
                'clinicType': 'all',
                'targetPageNo': str(int(current_page)+1)
            }

            yield scrapy.FormRequest.from_response(response, formdata=data, callback=self.parse_page)
