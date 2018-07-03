# -*- coding: utf-8 -*-
import scrapy
from item_test.items import ItemTestItem

class ItemtestSpider(scrapy.Spider):
    name = 'ItemTest'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']

    def parse(self, response):
        papers = response.xpath(".//*[@class='day']")
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0].encode('utf-8')
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0].encode('utf-8')
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0].encode('utf-8')
            content = paper.xpath("//*[@class='postCon']/div/text()").extract()[0].encode('utf-8')
            item = ItemTestItem(url=url, title=title, time=time, content=content)
            yield item

        pass
