import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'texto': quote.xpath('span[@class="text"]/text()').get(),
                'autor': quote.xpath('span/small[@class="author"]/text()').get(),
            }

        # Seguir a la siguiente página si existe
        siguiente_pagina = response.xpath('//li[@class="next"]/a/@href').get()
        if siguiente_pagina:
            yield response.follow(siguiente_pagina, self.parse)
