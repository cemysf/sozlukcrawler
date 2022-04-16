# -*- coding: utf-8 -*-
__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

import logging
from scrapy.http import Request
from scrapy.exceptions import CloseSpider

from datetime import datetime

from . import GenericSozlukSpider
from ..items import Girdi


class EksisozlukBaslikSpider(GenericSozlukSpider):
    name = 'eksisozluk'

    def __init__(self, **kwargs):
        super(EksisozlukBaslikSpider, self).__init__(**kwargs)
        self.allowed_domains = ['eksisozluk.com']

    def parse(self, response):
        self.log("PARSING: %s" % response.request.url, level=logging.INFO)

        items_to_scrape = response.xpath('//*[@id="entry-item-list"]/li[@data-author]')
        if len(items_to_scrape) == 0:
            self.log("!!! No item to parse found. It may indicate a problem with HTML !!!",
                     level=logging.ERROR)
            raise CloseSpider('no_item_found')

        for sel in items_to_scrape:
            girdi_id = sel.xpath('./@data-id').extract()[0]
            baslik_id = response.xpath('//*[@id="title"]/a/@href').re(r'--(\d*)')[0]
            baslik = response.xpath('//*[@id="title"]/a/span/text()').extract()[0]
            date = sel.xpath('./footer/div[@class="info"]/div[@class="entry-footer-bottom"]/div[@class="footer-info"]/div[2]/a/text()').re(r'\d{2}[.]\d{2}[.]\d{4} \d{2}[:]\d{2}')[0]
            text = sel.xpath('string(./div)').extract()[0]
            linkler = sel.xpath('./div/a/@href').extract()
            nick = sel.xpath('./@data-author').extract()[0]

            item = Girdi()
            item['source'] = self.name
            item['baslik'] = baslik
            item['girdi_id'] = girdi_id
            item['baslik_id'] = baslik_id
            item['datetime'] = datetime.strptime(date, '%d.%m.%Y %H:%M')
            item['text'] = text
            item['linkler'] = linkler
            item['nick'] = nick

            yield item

        # Sozluk sayfalamayi javascript ile yapiyor, dolayisi ile sayfa linkini XPath ile alamiyoruz ancak kacinci
        # sayfada oldugumuz ve son sayfa html icerisinde yer aliyor. Bu bilgileri kullanarak crawl edilecek bir
        # sonraki sayfanin adresini belirle. SSG degistirmez umarim :(
        current_page = int(response.xpath('(//div[@class="pager"])[1]/@data-currentpage').extract()[0])
        page_count = int(response.xpath('(//div[@class="pager"])[1]/@data-pagecount').extract()[0])

        current_url = response.request.url.split('?p')[0]

        next_page = current_page + 1
        if page_count >= next_page:
        # if current_page < 1:
            yield Request('%s?p=%s' % (current_url, next_page))
