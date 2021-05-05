import scrapy

class EtuoviScraperSpider(scrapy.Spider):
    name = 'etuovi_scraper'
    allowed_domains = ['etuovi.com']
    # assing a product-review-page url below
    start_urls = ['https://www.etuovi.com/myytavat-asunnot/tampere?haku=M1644131810']
    
    def parse(self, response):
        
        osoite = response.css('.flexboxgrid__col-xs-12__1I1LS.flexboxgrid__col-sm-7__1EzZq.flexboxgrid__col-md-9__2kjy7.flexboxgrid__col-lg-9__M7bfm.styles__infoArea__2yhEL > div.styles__cardTitle__14F5m > div.flexboxgrid__row__wfmuy > div > h4')
        
        kadut = []
        kaupunginosat = []
        for i in range(len(osoite)):
            osoite[i] = "".join(osoite[i].css('::text').extract()).strip()
            katu, kaupunginosa, kaupunki = osoite[i].split(', ')
            kadut.append(katu)
            kaupunginosat.append(kaupunginosa)

        hinta = response.css('.flexboxgrid__col-xs-12__1I1LS.flexboxgrid__col-sm-7__1EzZq.flexboxgrid__col-md-9__2kjy7.flexboxgrid__col-lg-9__M7bfm.styles__infoArea__2yhEL > div.styles__cardTitle__14F5m > div.styles__itemInfo__oDGHu > div > div.flexboxgrid__col-xs-4__p2Lev.flexboxgrid__col-md-4__2DYW- > span')
        
        for i in range(len(hinta)):
            hinta[i] = "".join(hinta[i].css('::text').extract()).strip()
            
        ala = response.css('.flexboxgrid__col-xs-12__1I1LS.flexboxgrid__col-sm-7__1EzZq.flexboxgrid__col-md-9__2kjy7.flexboxgrid__col-lg-9__M7bfm.styles__infoArea__2yhEL > div.styles__cardTitle__14F5m > div.styles__itemInfo__oDGHu > div > div.flexboxgrid__col-xs__26GXk.flexboxgrid__col-md-4__2DYW- > span')
            
        for i in range(len(ala)):
            ala[i] = "".join(ala[i].css('::text').extract()).strip()
            
        vuosi = response.css('.flexboxgrid__col-xs-12__1I1LS.flexboxgrid__col-sm-7__1EzZq.flexboxgrid__col-md-9__2kjy7.flexboxgrid__col-lg-9__M7bfm.styles__infoArea__2yhEL > div.styles__cardTitle__14F5m > div.styles__itemInfo__oDGHu > div > div.flexboxgrid__col-xs-3__3Kf8r.flexboxgrid__col-md-4__2DYW- > span')
            
        for i in range(len(vuosi)):
            vuosi[i] = "".join(vuosi[i].css('::text').extract()).strip()
            

        for i in range(len(osoite)):
            review = {
                'osoite': kadut[i],
                'kaupunginosa': kaupunginosat[i],
                'hinta': hinta[i],
                'koko': ala[i],
                'vuosi': vuosi[i],
            }
            yield review
            
        for i in range (2,27):    
            next_page_url = 'https://www.etuovi.com/myytavat-asunnot/tampere?haku=M1644131810&sivu=' + str(i)
            yield response.follow(next_page_url, self.parse)