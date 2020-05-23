#WARNING!!!!!
#IT IS NOT ALLOWED TO ALL WEBSITES. BEFORE USING IT,YOU MUST BE SURE THAT THE WEBSITE COMMITS THE EXPORT OF DATA FROM THIS.
# -*- coding: utf-8 -*-
import scrapy
from ..items import WebsitescrapItem 

class WebSpiderSpider(scrapy.Spider):
    name = 'web_spider'
    start_urls = ['# ADD THE URL FROM THE PAGE WHERE YOU WANT TO TAKE THE DATA']

    def parse(self, response):

        items = WebsitescrapItem()
        product_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]').css('::text').extract()
        product_price = response.css('.a-offscreen').css('::text').extract()
        product_img = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-image", " " ))]/@src').getall()
        
        
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_img'] = product_img

        yield items


