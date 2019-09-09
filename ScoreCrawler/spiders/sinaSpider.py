import scrapy
from ScoreCrawler.items import ScorecrawlerItem
import json

class sinaSpider(scrapy.Spider):
    name = "sinaSpider"
    allowed_domains = ["kaoshi.edu.sina.com.cn",]
    start_urls = []
    for i in range(1,32):
        start_urls.append("http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=&local=%d&provid=&batch=&syear=&page=1"%i)


    def parse(self, response):
        lines = response.xpath('//tr[@class="tbl2tbody"]')
        for line in lines:
            item = ScorecrawlerItem()
            item["univName"] = line.xpath('td/a[@class="blue"]/text()').extract()[0]
            item["positon"] = line.xpath('td[2]/text()').extract()[0]
            item["category"] = line.xpath('td[3]/text()').extract()[0]
            item["batch"] = line.xpath('td[4]/text()').extract()[0]
            item["year"] = line.xpath('td[5]/text()').extract()[0]
            item["highestScore"] = line.xpath('td[6]/text()').extract()[0]
            item["averageScore"] = line.xpath('td[7]/text()').extract()[0]
            # filename = r"./univFile/" + item["univName"] + item["positon"] + item["category"] + item["batch"] + item["year"] +'.json'
            # with open(filename,'w',encoding='UTF-8') as f:
            #     f.write(json.dumps(dict(item),ensure_ascii=False))
            yield item

            thisUrl = response.url
            # url长成这样：http://kaoshi.edu.sina.com.cn/college/scorelist?tab=&wl=&local=1&provid=&batch=&syear=&page=3
            thisPage = thisUrl[thisUrl.find('page=')+5:] # url中page后面的数
            nextPage = str(int(thisPage)+1)
            thisOther = thisUrl[:thisUrl.find('page=')+5] # url中除了“page后面的数”之外的字段
            nextUrl = thisOther + nextPage

            yield scrapy.Request(url=nextUrl,callback=self.parse)








