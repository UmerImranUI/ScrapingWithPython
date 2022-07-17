from urllib.request import Request
import scrapy
import re

def cleanup(input_string):# to cleanup
    #\r \n \t trailing space
    return re.sub(r'[\\r\\n\\t@]','',input_string).strip()
class NflSpider(scrapy.Spider):
    name = 'nfl'
    start_urls = ['http://www.nfl.com/']

    def parse(self, response):
        # all_players=response.css('#results::attr(href)').getall
        # link= response.urljoin(player)
        # yield Request(url=link, callback=self.parse_profile)


        all_players=response.css('#results::attr(href)').getall
        for player in all_players:
            link= response.urljoin(player)
            yield Request(url=link, callback=self.parse_profile)

        

        #to do: write pagination code
        next_page_url = response.urljoin(next_page_url)
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            yield Request(url=next_page_url, callback=self.parse)
        

    def parse_profile(self, response):
        link = response.urljoin("gamelogs")
        yield Request(url=link, callback=self.parse_log)

    def parse_log(self, response):
        player_name = response.css('.player-name::text').get()
        year=response.css('table')

        for season in response.css('table'):
            #process each table one by one
            season_name=season.css('thead>tr:nth-child(1)>td:nth-child(1)::text').get()

            #process each row one by one
            for week in season.css('tbody>tr'):
                second_td = week.css('td:nth-child(2)::text').get()
                if second_td is None:
                    continue
                elif second_td and 'TOTAL' in second_td:
                    continue


                
                item={
                    'player_name':player_name,
                    'year':year,
                    'season_name':season_name,
                    'week_num':week.css('td:nth-child(1)::text').get(),
                    'date_played':week.css('td:nth-child(2)::text').get(),
                    'opp':week.css('td:nth-child(3) a:last-child::text').get(),
                    'g':week.css('td:nth-child(5)::text').get(),
                    'gs':week.css('td:nth=child(6)::text').get(),
                    'url_l':response.url



                }


