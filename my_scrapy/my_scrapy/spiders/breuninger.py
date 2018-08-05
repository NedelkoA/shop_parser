import scrapy
from ..items import ProductItem


class BreuningerSpider(scrapy.Spider):
    name = 'breuninger'
    allowed_urls = ['breuninger.com']
    start_urls = [
        'https://www.breuninger.com/damen/schuhe',
        'https://www.breuninger.com/damen/bekleidung',
        'https://www.breuninger.com/herren/schuhe',
        'https://www.breuninger.com/herren/bekleidung'
    ]

    def parse(self, response):
        urls_post = response.xpath(
            '//div[contains(@class,"shop-grid-column")]'
            '/suchen-produkt-stage/suchen-produkt/a/@href'
        ).extract()
        for url in urls_post:
            yield scrapy.Request('https://www.breuninger.com'+url, callback=self.parse_post)

    def parse_post(self, response):
        item = ProductItem()
        item['brand'] = self.parse_name(response)[0]
        item['name'] = self.parse_name(response)[1]
        item['size'] = self.parse_size(response)
        item['description'] = self.parse_description(response)
        item['price'] = self.parse_price(response)
        item['currency'] = self.parse_currency(response)
        item['image'] = self.parse_images(response)
        yield item

    def parse_name(self, response):
        name = response.xpath('//span[@itemprop="name"]/text()').extract()
        return name

    def parse_size(self, response):
        size = response.xpath('//ul[@class="bewerten-groessen__list"]//text()').extract()
        return size

    def parse_description(self, response):
        description = response.xpath('//div[@itemprop="description"]//text()').extract()
        return description

    def parse_price(self, response):
        price = response.xpath('//meta[@itemprop="price"]/@content').extract()
        return price

    def parse_currency(self, response):
        currency = response.xpath('//meta[@itemprop="priceCurrency"]/@content').extract()
        return currency

    def parse_images(self, response):
        images = response.xpath('//img[contains(@class,"bewerten-slider-vertical__image")]/@src').extract()
        return images
