from scrapy.selector import Selector
from scrapy.http import HtmlResponse

import scrapy
from scrapy.crawler import CrawlerProcess


### ########################
# configure PPTV export behaviour
###########################
pptv_movie_w = open('pptv_movie.txt', 'w')
pptv_tv_w = open('pptv_tv.txt', 'w')
pptv_cartoon_w = open('pptv_cartoon.txt', 'w')

def pptv_movie_export(item):
    pptv_movie_w.write(item.encode("utf-8").strip() + '\n')

def pptv_tv_export(item):
    pptv_tv_w.write(item.encode("utf-8").strip() + '\n')

def pptv_cartoon_export(item):
    pptv_cartoon_w.write(item.encode("utf-8").strip() + '\n')

pptv_options = {1    :   pptv_movie_export,
                    2   :   pptv_tv_export,
                    3   :   pptv_cartoon_export,
}

### ########################
# configure Iqiyi export behaviour
###########################
iqiyi_movie_w = open('iqiyi_movie.txt', 'w')
iqiyi_tv_w = open('iqiyi_tv.txt', 'w')
iqiyi_doco_w = open('iqiyi_doco.txt', 'w')
iqiyi_cartoon_w = open('iqiyi_cartoon.txt', 'w')
iqiyi_webmovie_w = open('iqiyi_webmovie.txt', 'w')

def iqiyi_movie_export(item):
    iqiyi_movie_w.write(item.encode("utf-8").strip() + '\n')

def iqiyi_tv_export(item):
    iqiyi_tv_w.write(item.encode("utf-8").strip() + '\n')

def iqiyi_doco_export(item):
    iqiyi_doco_w.write(item.encode("utf-8").strip() + '\n')

def iqiyi_cartoon_export(item):
    iqiyi_cartoon_w.write(item.encode("utf-8").strip() + '\n')

def iqiyi_webmovie_export(item):
    iqiyi_webmovie_w.write(item.encode("utf-8").strip() + '\n')

iqiyi_options = {1    :   iqiyi_movie_export,
                    2   :   iqiyi_tv_export,
                    3   :   iqiyi_doco_export,
                    4   :   iqiyi_cartoon_export,
                    16  :   iqiyi_webmovie_export,
}



### ########################
# configure Tencent export behaviour
###########################
tencent_movie_w = open('tencent_movie.txt', 'w')
tencent_tv_w = open('tencent_tv.txt', 'w')
tencent_doco_w = open('tencent_doco.txt', 'w')
tencent_cartoon_w = open('tencent_cartoon.txt', 'w')

def tencent_movie_export(item):
    tencent_movie_w.write(item.encode("utf-8").strip() + '\n')

def tencent_tv_export(item):
    tencent_tv_w.write(item.encode("utf-8").strip() + '\n')

def tencent_doco_export(item):
    tencent_doco_w.write(item.encode("utf-8").strip() + '\n')

def tencent_cartoon_export(item):
    tencent_cartoon_w.write(item.encode("utf-8").strip() + '\n')

tencent_options = {'movie'    :   tencent_movie_export,
                    'tv'  :   tencent_tv_export,
                    'doco'   :   tencent_doco_export,
                    'cartoon'   :   tencent_cartoon_export,
}

### ########################
# configure Funtv export behaviour
###########################
funtv_movie_w = open('funtv_movie.txt', 'w')
funtv_minimovie_w = open('funtv_minimovie.txt', 'w')
funtv_tv_w = open('funtv_tv.txt', 'w')
funtv_cartoon_w = open('funtv_cartoon.txt', 'w')
funtv_show_w = open('funtv_show.txt', 'w')

def funtv_movie_export(item):
    funtv_movie_w.write(item.encode("utf-8").strip() + '\n')

def funtv_minimovie_export(item):
    funtv_minimovie_w.write(item.encode("utf-8").strip() + '\n')

def funtv_tv_export(item):
    funtv_tv_w.write(item.encode("utf-8").strip() + '\n')

def funtv_cartoon_export(item):
    funtv_cartoon_w.write(item.encode("utf-8").strip() + '\n')

def funtv_show_export(item):
    funtv_show_w.write(item.encode("utf-8").strip() + '\n')

funtv_options = {0    :   funtv_movie_export,
                    1  :   funtv_minimovie_export,
                    2   :   funtv_tv_export,
                    3   :   funtv_cartoon_export,
                    4   :   funtv_show_export,
}

### ########################
# configure 2345(Essw) export behaviour
###########################
essw_movie_w = open('essw_movie.txt', 'w')
essw_tv_w = open('essw_tv.txt', 'w')
essw_cartoon_w = open('essw_cartoon.txt', 'w')
essw_show_w = open('essw_show.txt', 'w')

def essw_movie_export(item):
    essw_movie_w.write(item.encode("utf-8").strip() + '\n')

def essw_tv_export(item):
    essw_tv_w.write(item.encode("utf-8").strip() + '\n')

def essw_cartoon_export(item):
    tencent_cartoon_w.write(item.encode("utf-8").strip() + '\n')

def essw_show_export(item):
    essw_show_w.write(item.encode("utf-8").strip() + '\n')

essw_options = {0    :   essw_movie_export,
                    1   :   essw_tv_export,
                    2   :   essw_cartoon_export,
                    3  :   essw_show_export,
}


### ########################
# PPTV Spider Class
###########################
class PPTVSpider(scrapy.Spider):
    name = 'spidypptv'
    base_url = 'http://list.pptv.com/channel_list.html?page=%s&type=%s&sort=1'
    # type 1: movie, type 2: tv series, type 3: cartoon
    pptv_type = 1
    # start page is 1 
    page = 1
    start_urls = [base_url %(page, pptv_type)]   # process.start() begin from here
    # download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('//li//a//p[re:test(@class, "ui-txt")]//span/text()').extract()
        # write movie names into file
        for item in names: 
            pptv_options[self.pptv_type](item)
        # continue to fetch if has next page (these 3 types has no more than 150  pages)
        if self.page < 150:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url % (self.page, self.pptv_type))
        elif self.pptv_type < 3:
            self.pptv_type = self.pptv_type + 1 # next type
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.page, self.pptv_type))

### ########################
# Iqiyi Spider Class
###########################
class IqiyiSpider(scrapy.Spider):
    name = 'spidyiqiyi'
    base_url = 'http://list.iqiyi.com/www/%s/-------------4-%s-1-iqiyi--.html'
    # type 1: movie, type 2: tv series, type 3: documentaires, type 4: cartoon, type 16: internet movie
    iqiyi_type_list = [1, 2, 3, 4, 16]
    iqiyi_type = iqiyi_type_list[0]  # initial type
    type_count = 0
    # start page is 1 
    page = 1
    start_urls = [base_url %(iqiyi_type, page)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('//div[@class="page-list"]//div//div//div[@class="wrapper-cols"] \
                //div//li//div[@class="site-piclist_info"]//a/text()').extract()
        # write movie names into file
        for item in names: 
            iqiyi_options[self.iqiyi_type](item)
        # continue to fetch if has next page (Iqiyi has no more than 30  pages in each type)
        if self.page < 30:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.iqiyi_type, self.page))
        elif self.type_count < len(self.iqiyi_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.iqiyi_type = self.iqiyi_type_list[self.type_count] # set type number
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.iqiyi_type, self.page))

### ########################
# Tencent Spider Class
###########################
class TencentSpider(scrapy.Spider):
    name = 'spidytencent'
    base_url = 'http://v.qq.com/x/list/%s?&offset=%s'
    tencent_type_list = ['movie', 'tv', 'doco', 'cartoon']
    tencent_type = tencent_type_list[0]  # initial type
    type_count = 0
    # start offset is 0, each page has 30 items, offset increment by setp of 30
    offset = 0
    start_urls = [base_url %(tencent_type, offset)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('/html/body/div[3]/div/div/div[1]/div[2]/div/ul/li/div[1]/strong/a/text()').extract()
        # write movie names into file
        for item in names: 
            tencent_options[self.tencent_type](item)
        # continue to fetch if has next page (Tencent has no more than 200  pages in each type)
        if self.offset < 6000:
            self.offset = self.offset + 30   # next offset
            yield scrapy.Request(self.base_url %(self.tencent_type, self.offset))
        elif self.type_count < len(self.tencent_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.tencent_type = self.tencent_type_list[self.type_count] # set type number
            self.offset = 0   # reset to start offset
            yield scrapy.Request(self.base_url %(self.tencent_type, self.offset))

### ########################
# Funtv Spider Class
###########################
class FuntvSpider(scrapy.Spider):
    name = 'spidyfuntv'
    base_url = 'http://www.fun.tv/retrieve/%s.pg-%s.uc-205'
    # initial type
    type_count = 0
    funtv_type_list = ['c-e794b5e5bdb1', 'c-e5beaee794b5e5bdb1', \
                            'c-e794b5e8a786e589a7', 'c-e58aa8e6bcab', 'c-e7bbbce889ba']
    funtv_type = funtv_type_list[0] # start type
    # initial page
    page = 1
    page_bound = 100
    start_urls = [base_url %(funtv_type, page)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('/html/body/div[5]/div/div[3]/div/div/div[2]/h3/a/text()').extract()
        # write movie names into file
        for item in names: 
            funtv_options[self.type_count](item)
        # continue to fetch if has next page (funtv has no more than 200  pages in each type)
        if self.page < self.page_bound:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.funtv_type, self.page))
        elif self.type_count < len(self.funtv_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.funtv_type = self.funtv_type_list[self.type_count] # set type number
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.funtv_type, self.page))

### ########################
# 2345(essw) Spider Class
###########################
class EsswSpider(scrapy.Spider):
    name = 'spidyessw'
    handle_httpstatus_list = [404]
    # base urls
    url_movie = 'http://dianying.2345.com/list/-------%s.html'
    url_tv = 'http://tv.2345.com/-----%s.html'
    url_cartoon = 'http://dongman.2345.com/lt/%s'
    url_show = 'http://kan.2345.com/zongyi/lpxdefault/%s/'
    # urls to loop 
    urls = [url_movie, url_tv, url_cartoon, url_show]
    url_count = 0
    base_url = urls[url_count]  # start url
    # corresponding xpath format
    xpath_movie = '//*[@id="contentList"]/ul/li/div[2]/span[1]/em/a/text()'
    xpath_tv = '//*[@id="contentList"]/ul/li/div[2]/span[1]/a/text()'
    xpath_cartoon = '//*[@id="contentList"]/ul/li/span/a/text()'
    xpath_show = '//*[@id="contentList"]/ul/li/div[2]/span/a/text()'
    xpaths = [xpath_movie, xpath_tv, xpath_cartoon, xpath_show]
    # start page is 1 
    page = 1
    # page bound
    page_bound = 100
    start_urls = [url_show % page]
    # download_delay = 1.5    # prevent censorship

    def parse(self, response):

        names = Selector(text=response.body).xpath(self.xpaths[self.url_count]).extract()
        # write movie names into file
        for item in names: 
            essw_options[self.url_count](item)
 
        # continue to fetch if has next page (essw has no more than 200  pages in each type)
        if self.page < self.page_bound:
            if response.status is 404: # handle 404 error
                pass
            elif response.status is 200:    # page loaded successfully
                self.page = self.page + 1  # next page
                yield scrapy.Request(self.base_url % self.page)
            else:
                print "holy god, what happened?"
        elif self.url_count < len(self.urls)-1:
            self.url_count = self.url_count + 1 # next url
            self.base_url = self.urls[self.url_count] # reset url
            self.page = 1   # reset start page
            yield scrapy.Request(self.base_url % self.page)

if __name__=="__main__":

    process = CrawlerProcess()

    process.crawl(EsswSpider)
    process.start()

    pptv_movie_w.close()
    pptv_tv_w.close()

