import scrapy

class SpiderClass(scrapy.Spider):
    name = 'quotes'
    def start_request(self):
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/']
    
        for url in urls:
            result = scrapy.Request(url=url, callback=self.parse)
            yield result
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' % page
    
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('saved')
