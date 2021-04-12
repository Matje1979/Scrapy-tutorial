import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem
from selenium import webdriver
from scrapy.http import FormRequest
#scrapy.utils.response import open_in_browser

##Logging into websites

    class QuoteSpider(scrapy.Spider):
        name='quotes'
        start_urls = [
            'http://quotes.toscrape.com/login'
        ]

        def parse(self, response):
            token = response.css('form input::attr(value)').extract_first()
            print (token)
            return FormRequest.from_response(response, formdata = {
                'csrf_token' : token,
                'username' : 'njnlk@gmail.com',
                'password' : 'caqqedqd'
                }, callback=self.start_scraping) 

        def start_scraping(self, response):
            open_in_browser(response)
            items = QuotetutorialItem()

            all_div_quotes = response.css('div.quote')

            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

            next_page = response.css('li.next a::attr(href)').get()
            print (next_page)
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
            

##To check if login works search for 302 (redirect) or add above scrapy.utils.response import open_in_browser


