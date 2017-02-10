import json
import scrapy
from scrapy.crawler import CrawlerProcess

# configure export behaviour
fname_export = "export.txt"
export_w = open(fname_export, 'w')

class SpidyQuotesSpider(scrapy.Spider):
    name = 'spidyquotes'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5
 
    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            export_w.write(item.get('text').encode("utf-8") + '\n')
            # yield {
            #     'text': item.get('text'),
            #     'author': item.get('author', {}).get('name'),
            #     'tags': item.get('tags'),
            # }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)

if __name__=="__main__":

    process = CrawlerProcess()

    process.crawl(SpidyQuotesSpider)
    process.start()

    export_w.close()
