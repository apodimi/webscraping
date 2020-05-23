# -*- coding: utf-8 -*-
import scrapy
from ..items import WebsitescrapItem 

class WebSpiderSpider(scrapy.Spider):
    name = 'web_spider'
    start_urls = ['https://www.amazon.com/s?k=pc+case&rh=n%3A541966%2Cn%3A572238&dc&qid=1590262124&rnid=2941120011&ref=sr_nr_n_2']

    def parse(self, response):

        items = WebsitescrapItem()
        product_name = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "a-color-base", " " )) and contains(concat( " ", @class, " " ), concat( " ", "a-text-normal", " " ))]').css('::text').extract()
        product_price = response.css('.a-offscreen').css('::text').extract()
        product_img = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-image", " " ))]/@src').getall()
        
        
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_img'] = product_img

        yield items


