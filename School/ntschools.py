
import scrapy
import json


class School(scrapy.Spider):
    name = "schoolspi"
    start_urls = ['https://directory.ntschools.net/#/schools']

    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://directory.ntschools.net/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'X-Requested-With': 'Fetch',
    }

    def parse(self, response):
        request = scrapy.Request(
            url='https://directory.ntschools.net/api/System/GetAllSchools', callback=self.parse_api, headers=self.headers)
        yield request

    def parse_api(self, response):
        base_url = [
            "https://directory.ntschools.net/api/System/GetSchool?itSchoolCode=acacisch"]
        raw_data = response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school['itSchoolCode']
            
            request = scrapy.Request(
                f"https://directory.ntschools.net/api/System/GetSchool?itSchoolCode={school_code}", callback=self.parse_school, headers=self.headers
            )
            yield request

    def parse_school(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        yield{
            'Name': data['name'],
            'PhysicalAddress': data['physicalAddress'],
            'PostalAddress': data['postalAddress']['displayAddress'],
            'Email': data['mail'],
            'Phone': data['telephoneNumber'],
        }
