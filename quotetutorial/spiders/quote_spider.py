    import scrapy

    from scrapy.http import FormRequest

    from ..items import QuotetutorialItem

    from selenium import webdriver

    # class QuoteSpider(scrapy.Spider):
    #     name='quotes'
    #     start_urls = [
    #         'https://katastar.rgz.gov.rs/StambeneZajednice/'
    #     ]
    #     page_num = 1
    #     url_lists=[]

    #     def parse(self, response):
    #         print("******************* Hello **************************")
            
    #         yield FormRequest.from_response(response, formdata={'ctl00$Body$ctl00$ctl00$PretragaStambenihZajednica$SelectOpstina$Opstina':'70017', '__EVENTARGUMENT': next_page}, callback=self.parse_result)

    #     # def parse_u(self, response):
    #  #         desc = response.css(".desc::text").extract()
    #  #         yield desc

    #     # def u_func(self, response):
    #     #   next_page = response.css("li.next a::attr(href)").get()x

    #     #     if next_page is not None:
    #     #       yield response.follow(next_page, callback=self.parse_u)

    #     # def new_func(self):
    #     #   next_page = response.css("li.next a::attr(href)").get()

    #     #     if next_page is not None:
    #     #       yield response.follow(next_page, callback=self.u_func)


    #     def parse_result(self, response):

    #         print("******************* Hello again *************")

    #         all_div_quotes = response.css(".view-link")
    #         # print ("All_div_quotes", all_div_quotes)

    #         # url_list=[]

    #         while QuoteSpider.page_num < 4:

    #             for quote in all_div_quotes:
                    
    #                 title = quote.css("::text").extract()
    #                 print ("##########################################################This is a quote: ", title)
    #                 detail_page = quote.css(".view-link::attr(href)").get()
    #                 full_url = 'https://katastar.rgz.gov.rs' + detail_page
    #                 # url_list.append(full_url)
    #                 print ("*******This is the full_url******")
    #                 print (full_url)
    #                 items = QuotetutorialItem()
    #                 items['title'] = title
    #                 yield scrapy.Request(full_url, callback=self.parse_new, meta={'items':items})
    #             # QuoteSpider.url_lists.append(url_list)
    #             QuoteSpider.page_num +=1



    #         # yield scrapy.Request('https://katastar.rgz.gov.rs/StambeneZajednice/', callback=self.parse)

    #             # author = quote.css(".author::text").extract()
    #             # description = new_func()
    #             # tag = quote.css(".tag::text").extract()

    #             # items['title'] = title
    #             # items['author'] = author
    #             # items['tag'] = tag

    #             # yield items

            
           
    #         yield scrapy.Request('https://katastar.rgz.gov.rs', callback=self.parse)
    #         #     yield response.follow(next_page, callback=self.parse)

    #     def parse_new(items, response):
    #         items = response.request.meta['items']
    #         print("******************* Hello again again ******************")
    #         address = response.css(".data td::text").extract_first()
    #         items['author'] = address
            
    #         # print ("This is the address:")
    #         # print (address)
    #         yield items


    class QuoteSpider(scrapy.Spider):
        name='quotes'
        start_urls = [
            'http://quotes.toscrape.com/'
        ]
        next_page = 2

        def parse(self, response):
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

            ##For scraping pages with pagination:
            # next_page = "'http://quotes.toscrape.com/" + QuoteSpider.next_page
            # if QuoteSpider.next_page > 11:
            #     yield response.follow(next_page, callback=self.parse)
            # QuoteSpider.next_page += 1
