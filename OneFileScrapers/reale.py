import scrapy


class RealeSpider(scrapy.Spider):
    name = 'reale'
    start_urls = ['https://www.realestate.com.au/']

    def parse(self, response):
        url='https://www.realestate.com.au/buy/in-2010%3b+2011/list-1?activeSort=list-date'
        headers = {
                'authority': 'www.realestate.com.au',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'no-cache',
                'cookie': 'mid=9340563328808081233; reauid=2cf57468d64a00004d91c362a7000000c6710000; Country=PK; split_audience=e; fullstory_audience_split=B; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; _sp_ses.2fe7=*; _gcl_au=1.1.726911411.1656983889; _gid=GA1.3.1514122662.1656983889; s_ecid=MCMID%7C19531496218760631960245455466038097757; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19179%7CMCMID%7C19531496218760631960245455466038097757%7CMCAAMLH-1657588688%7C3%7CMCAAMB-1657588688%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1656991088s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; DM_SitId1464=true; DM_SitId1464SecId12708=true; DM_SitIdT1464=true; DM_SitId1464SecIdT12708=true; _fbp=fb.2.1656983891977.894292370; VT_LANG=language%3Den-US; KP2_UIDz-ssn=02zUthmYy5HVUZxpBpvueH8EuK9Q7sIUTSystzcWCrIvgf2DLODkk2QhD9ONcukAtSc5tGQCFGlVKR74mxNgq3xooaAKzR7vMLSdjK5bsD2m6vjoiJDH7KS6vWPT4WT12xXIEv8YKSDX24iOiAQO5MsjZLf; KP2_UIDz=02zUthmYy5HVUZxpBpvueH8EuK9Q7sIUTSystzcWCrIvgf2DLODkk2QhD9ONcukAtSc5tGQCFGlVKR74mxNgq3xooaAKzR7vMLSdjK5bsD2m6vjoiJDH7KS6vWPT4WT12xXIEv8YKSDX24iOiAQO5MsjZLf; pageview_counter.srs=8; utag_main=v_id:0181cbef9e87001f6116935aaa7d0506f00ad067009dc$_sn:1$_se:28$_ss:0$_st:1656987550559$ses_id:1656983887496%3Bexp-session$_pn:3%3Bexp-session$vapi_domain:realestate.com.au$dc_visit:1$dc_event:10%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; _sp_id.2fe7=ee503602-4fdf-4463-b204-e2aa891e1c12.1656983889.1.1656985751.1656983889.90d4fc60-da2d-42f0-968b-eeb272985dda; _ga_F962Q8PWJ0=GS1.1.1656983888.1.1.1656985751.0; _ga=GA1.1.629834497.1656983889; nol_fpid=iqidzorvdadk7dj1uvevvmbamzkyv1656983890|1656983890952|1656985752552|1656985761239; External=%2FAPPNEXUS%3D364976707388791753%2FCASALE%3DYqqymq05nwvH7JB8ltoGQAAA%25264454%2FOPENX%3D7111fe5f-aca4-43cb-8677-218844ff762e%2FPUBMATIC%3D6D03E003-7A0E-4CA9-B79F-CE026F7932CE%2FRUBICON%3DL4JDFELV-U-IZQ1%2FTRIPLELIFT%3D2416678842741003129001%2F_EXP%3D1688521762%2F_exp%3D1688521770; cto_bundle=HRz2Pl9JSEJGWm83aWozTERtWEJmWWlNZzJwY0o3bjU5TkFGcXRxckVVQXY1c1k4U2ZDZzEzQVVPNUZveVRka2pnQ25GeElwNmQwN2MxQVp2TlpQcyUyQjdQRjRtZjVaS0s1a01sUjZ6SkRiSkMlMkJVaTJ4Ujh3d2pWU1h4dFZBT0tnNXdwRzEzRXI1UTh6Q3M2MEtNUkNFWjNjem9KNksxclJjNjVqWmx0TG5EVThjMm00JTNE; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Fin-2010%253b%2B2011%2Flist-47%3FactiveSort%3Dlist-date~1656983960452%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Fin-2010%253b%2B2011%2Flist-1%3FactiveSort%3Dlist-date~1656983969241%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Fin-2010%253b%2B2011%2Flist-47%3FactiveSort%3Dlist-date~1656984185260%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Fin-2010%253b%2B2011%2Flist-1%3FactiveSort%3Dlist-date~1656985775184; Country=PK',
                'pragma': 'no-cache',
                'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'my-cool-project (http://example.com)'
            }

        yield scrapy.FormRequest(url, headers=headers, callback= self.parse_detail)
        

    def parse_detail(self, response):
        pi=response.css('#listings-app-container > div.results-page > div.layout.layout--no-mobile-gutters.results-page__content > div.layout__content > div.divided-content > div.tiered-results-container > div > div:nth-child(8) > article > div.residential-card__content-wrapper > div.residential-card__content > div.piped-content > div > div:nth-child(2) > span').css('::text').extract_first()
        yield{
                'pi':pi
            }
