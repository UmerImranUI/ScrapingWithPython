import scrapy
from scrapy import FormRequest

class CasaSpider(scrapy.Spider):
    name = 'casa'
    start_urls = [
        'https://www.casablanca-bourse.com/bourseweb/Societe-Cote.aspx?codeValeur=12200']

    def parse(self, response):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        formdata = {
            'TopControl1$ScriptManager1': 'SocieteCotee1$UpdatePanel1|SocieteCotee1$LBFicheTech',
            '__EVENTTARGET': 'SocieteCotee1$LBFicheTech',
            'TopControl1$TxtRecherche': '',
            'TopControl1$txtValeur': '',
            'SocieteCotee1$ListScCote': '',
            'hiddenInputToUpdateATBuffer_CommonToolkitScripts': '1',
        }

        yield FormRequest.from_response(response, formdata=formdata, headers=
                                         headers, callback=self.tab2)

    def tab2(self, response):
        yield response.css('#SocieteCoteel_FicheeTechniquel-lblISIN ::text').get()
