from scrapy.selector import Selector
from scrapy.http import HtmlResponse

import scrapy
from scrapy.crawler import CrawlerProcess


###########################
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

###########################
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


###########################
# configure IqiyiLib export behaviour
###########################
iqiyilib_movie_w = open('iqiyilib_movie.txt', 'w')
iqiyilib_tv_w = open('iqiyilib_tv.txt', 'w')
iqiyilib_cartoon_w = open('iqiyilib_cartoon.txt', 'w')

def iqiyilib_movie_export(item):
    iqiyilib_movie_w.write(item.encode("utf-8").strip() + '\n')

def iqiyilib_tv_export(item):
    iqiyilib_tv_w.write(item.encode("utf-8").strip() + '\n')

def iqiyilib_cartoon_export(item):
    iqiyilib_cartoon_w.write(item.encode("utf-8").strip() + '\n')

iqiyilib_options = {0    :   iqiyilib_movie_export,
                    1  :   iqiyilib_tv_export,
                    2   :   iqiyilib_cartoon_export,
}

###########################
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

###########################
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

###########################
# configure Zaizai export behaviour
###########################
zaizai_movie_w = open('zaizai_movie.txt', 'w')
zaizai_tv_w = open('zaizai_tv.txt', 'w')
zaizai_cartoon_w = open('zaizai_cartoon.txt', 'w')

def zaizai_movie_export(item):
    zaizai_movie_w.write(item.encode("utf-8").strip() + '\n')

def zaizai_tv_export(item):
    zaizai_tv_w.write(item.encode("utf-8").strip() + '\n')

def zaizai_cartoon_export(item):
    zaizai_cartoon_w.write(item.encode("utf-8").strip() + '\n')

zaizai_options = dict()
for i in range(6):
    zaizai_options[i] = zaizai_movie_export
for i in range(6, 13):
    zaizai_options[i] = zaizai_tv_export
zaizai_options[13] = zaizai_cartoon_export
print zaizai_options

###########################
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


###########################
# configure 1905(Yjlw) export behaviour
###########################
yjlw_movie_w = open('yjlw_movie.txt', 'w')

def yjlw_movie_export(item):
    yjlw_movie_w.write(item.encode("utf-8").strip() + '\n')

yjlw_options = { 0   :   yjlw_movie_export }

###########################
# configure Youku export behaviour
###########################
youku_movie_w = open('youku_movie.txt', 'w')
youku_tv_w = open('youku_tv.txt', 'w')
youku_cartoon_w = open('youku_cartoon.txt', 'w')
youku_doco_w = open('youku_doco.txt', 'w')

def youku_movie_export(item):
    youku_movie_w.write(item.encode("utf-8").strip() + '\n')

def youku_tv_export(item):
    youku_tv_w.write(item.encode("utf-8").strip() + '\n')

def youku_cartoon_export(item):
    youku_cartoon_w.write(item.encode("utf-8").strip() + '\n')

def youku_doco_export(item):
    youku_doco_w.write(item.encode("utf-8").strip() + '\n')

youku_options = {0    :   youku_movie_export,
                    1  :   youku_tv_export,
                    2   :   youku_cartoon_export,
                    3   :   youku_doco_export,
}

###########################
# configure Xiazai export behaviour
###########################
xiazai_movie_w = open('xiazai_movie.txt', 'w')
xiazai_tv_w = open('xiazai_tv.txt', 'w')
xiazai_cartoon_w = open('xiazai_cartoon.txt', 'w')

def xiazai_movie_export(item):
    xiazai_movie_w.write(item.encode("utf-8").strip() + '\n')

def xiazai_tv_export(item):
    xiazai_tv_w.write(item.encode("utf-8").strip() + '\n')

def xiazai_cartoon_export(item):
    xiazai_cartoon_w.write(item.encode("utf-8").strip() + '\n')

xiazai_options = {0    :   xiazai_movie_export,
                    1  :   xiazai_tv_export,
                    2   :   xiazai_cartoon_export,
}

###################################################

###########################
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

###########################
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
    page_bound = 30 # no more than 30 pages each
    start_urls = [base_url %(iqiyi_type, page)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('/html/body/div[4]/div/div/div[3]/div/ul/li/div[2]/div[1]/p/a/text()').extract()
        # write movie names into file
        for item in names: 
            iqiyi_options[self.iqiyi_type](item)
        # continue to fetch if has next page (Iqiyi has no more than 30  pages in each type)
        if self.page < self.page_bound:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.iqiyi_type, self.page))
        elif self.type_count < len(self.iqiyi_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.iqiyi_type = self.iqiyi_type_list[self.type_count] # set type number
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.iqiyi_type, self.page))

###########################
# IqiyiLib Spider Class
###########################
class IqiyilibSpider(scrapy.Spider):
    name = 'spidyiqiyilib'
    base_url = 'http://www.iqiyi.com/lib/%s/%%2C%%2C_11_%s.html'
    # types
    iqiyilib_type_list = ['dianying', 'dianshiju', 'dongman']
    iqiyilib_type = iqiyilib_type_list[0]  # initial type
    type_count = 0
    # start page is 1 
    page = 1
    page_bound = 100    # all types have 100 pages
    start_urls = [base_url %(iqiyilib_type, page)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                .xpath('/html/body/div[2]/div[5]/div/div[2]/div/ul/li/div[2]/div[1]/p/a/text()').extract()
        # write movie names into file
        for item in names: 
            iqiyilib_options[self.type_count](item)
        # page loop
        if self.page < self.page_bound:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.iqiyilib_type, self.page))
        # type loop
        elif self.type_count < len(self.iqiyilib_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.iqiyilib_type = self.iqiyilib_type_list[self.type_count] # set type number
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.iqiyilib_type, self.page))

###########################
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

###########################
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

###########################
# Be7e(8e7e) Spider Class
###########################
class Be7eSpider(scrapy.Spider):
    name = 'spidybe7e'
    handle_httpstatus_list = [404]  # necessary to handle 404
    base_url = 'http://www.8e7e.com/vod-show-id-%s-p-%s.html'
    # types : movie 0-5, tv 6-12, cartoon 13
    ba7e_type_list = ['xj', 'dz', 'aq', 'kh', 'kb', 'jq', 'gc', 'tvb', \
                                'tw', 'hg', 'riben', 'om', 'tg', 'dh']
    ba7e_type = ba7e_type_list[0]  # initial type
    type_count = 0
    # start page is 1 
    page = 1
    page_bound = 700    # max 700 pages
    start_urls = [base_url %(ba7e_type, page)]   # process.start() begin from here
    download_delay = 1.5

    def parse(self, response):

        print response.body
        names = Selector(text=response.body) \
                        .xpath('/html/body/metaname/div[4]/div[1]/ul/li/a/span[2]/p[1]/text()').extract()
        # write movie names into file
        for item in names:
            # print item.encode("utf-8") 
            ba7e_options[self.type_count](item)
        # page loop
        if self.page < self.page_bound:
            # if response.status is 404: # handle 404 error
            #     pass
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.ba7e_type, self.page), \
                                                encoding="gb2312")  # encoding of response?
        # type loop
        elif self.type_count < len(self.ba7e_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.ba7e_type = self.ba7e_type_list[self.type_count] # set type number
            self.page = 1   # reset to start page
            yield scrapy.Request(self.base_url %(self.ba7e_type, self.page), \
                                                encoding="gb2312")

###########################
# Zaizai Spider Class
###########################
class ZaizaiSpider(scrapy.Spider):
    name = 'spidyzaizai'
    handle_httpstatus_list = [404]  # necessary to handle 404
    base_url = 'http://www.zaizai8.com/%s/index%s.html'
    # types : movie 0-5, tv 6-12, cartoon 13
    zaizai_type_list = ['xj', 'dz', 'aq', 'kh', 'kb', 'jq', 'gc', 'tvb',    \
                                'tw', 'hg', 'riben', 'om', 'tg', 'dh']
    zaizai_type = zaizai_type_list[0]  # initial type
    type_count = 0
    # start page is 1 
    start_page = 2
    page = start_page
    page_bound = 700    # max 700 pages
    start_urls = [base_url %(zaizai_type, page)]   # process.start() begin from here
    # download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body.decode('gbk')) \
                        .xpath('/html/body/metaname/div[4]/div[1]/ul/li/a/span[2]/p[1]/text()').extract()
        # write movie names into file
        for item in names:
            # print item 
            zaizai_options[self.type_count](item)
        # page loop, if 404 occurs, go to elif, next type
        if self.page < self.page_bound and response.status != 404:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.zaizai_type, self.page))
        # type loop
        elif self.type_count < len(self.zaizai_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.zaizai_type = self.zaizai_type_list[self.type_count] # set type number
            self.page = self.start_page   # reset to start_page
            yield scrapy.Request(self.base_url %(self.zaizai_type, self.page))

###########################
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
    xpath_movie = '//*[@id="contentList"]/ul/li/div[2]/span[1]/em/a/@text()'
    xpath_tv = '//*[@id="contentList"]/ul/li/div[2]/span[1]/a/@text()'
    xpath_cartoon = '//*[@id="contentList"]/ul/li/span/a/text()'
    xpath_show = '//*[@id="contentList"]/ul/li/div[2]/span/a/@text()'
    xpaths = [xpath_movie, xpath_tv, xpath_cartoon, xpath_show]
    # start page is 1 
    page = 1
    # page bound
    page_bound = 100
    start_urls = [url_show % page]
    # download_delay = 1.5    # prevent censorship

    def parse(self, response):

        # respond.body.decode('gbk') is necessary for this website
        names = Selector(text=response.body.decode('gbk')) \
                     .xpath(self.xpaths[self.url_count]).extract()
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
                print "holy god, what now?"
        elif self.url_count < len(self.urls)-1:
            self.url_count = self.url_count + 1 # next url
            self.base_url = self.urls[self.url_count] # reset url
            self.page = 1   # reset start page
            yield scrapy.Request(self.base_url % self.page)

###########################
# Yjlw Spider Class
###########################
class YjlwSpider(scrapy.Spider):
    name = 'spidyyjlw'
    handle_httpstatus_list = [404]  # necessary to handle 404
    base_url = 'http://www.1905.com/vod/list/n_1/o3p%s.html'
    # only one type, set to 0
    type_count = 0
    # start page is 1 
    start_page = 1
    page = start_page
    page_bound = 320    # max 320 pages
    start_urls = [base_url % page]   # process.start() begin from here
    # download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                        .xpath('//*[@id="content"]/section[4]/div/a/img/@alt').extract()
        # write movie names into file
        for item in names:
            # print item 
            yjlw_options[self.type_count](item)
        # page loop, if 404 occurs, go to elif, next type
        if self.page < self.page_bound and response.status != 404:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url % self.page)

###########################
# Youku Spider Class
###########################
class YoukuSpider(scrapy.Spider):
    name = 'spidyyouku'
    handle_httpstatus_list = [404]  # necessary to handle 404
    base_url = 'http://list.youku.com/category/show/c_%s_s_1_d_1_p_%s.html?spm=a2h1n.8251845.0.0'
    # types : movie 0-5, tv 6-12, cartoon 13
    youku_type_list = ['96', '97', '100', '84']
    youku_type = youku_type_list[0]  # initial type
    type_count = 0
    # start page is 1 
    start_page = 1 
    page = start_page
    page_bound = 30    # max 30 pages
    start_urls = [base_url %(youku_type, page)]   # process.start() begin from here
    # download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                        .xpath('/html/body/div[re:test(@class, "s-body")]' + \
                            '/div/div[2]/div[2]/ul/li/div/ul[2]/li[1]/a/text()').extract()
        # write movie names into file
        for item in names:
            # print item 
            youku_options[self.type_count](item)
        # page loop, if 404 occurs, go to elif, next type
        if self.page < self.page_bound and response.status != 404:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.youku_type, self.page))
        # type loop
        elif self.type_count < len(self.youku_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.youku_type = self.youku_type_list[self.type_count] # set type number
            self.page = self.start_page   # reset to start_page
            yield scrapy.Request(self.base_url %(self.youku_type, self.page))

###########################
# Xiazai Spider Class
###########################
class XiazaiSpider(scrapy.Spider):
    name = 'spidyxiazai'
    handle_httpstatus_list = [404]  # necessary to handle 404
    base_url = 'http://list.xiazai.kankan.com/type/%s/page%s/'
    # types : movie 0-5, tv 6-12, cartoon 13
    xiazai_type_list = ['movie', 'teleplay', 'anime']
    xiazai_type = xiazai_type_list[0]  # initial type
    type_count = 0
    # start page is 2 
    start_page = 2 
    page = start_page
    page_bound = 420    # max 416 pages
    start_urls = [base_url %(xiazai_type, page)]   # process.start() begin from here
    # download_delay = 1.5

    def parse(self, response):

        names = Selector(text=response.body) \
                        .xpath('//*[@id="results_big_box"]/div[2]/ul/li/h3/a/text()').extract()
        # write movie names into file
        for item in names:
            # print item 
            xiazai_options[self.type_count](item)
        # page loop, if 404 occurs, go to elif, next type
        if self.page < self.page_bound and response.status != 404:
            self.page = self.page + 1   # next page
            yield scrapy.Request(self.base_url %(self.xiazai_type, self.page))
        # type loop
        elif self.type_count < len(self.xiazai_type_list)-1:
            self.type_count = self.type_count + 1 # next type
            self.xiazai_type = self.xiazai_type_list[self.type_count] # set type number
            self.page = self.start_page   # reset to start_page
            yield scrapy.Request(self.base_url %(self.xiazai_type, self.page))

if __name__=="__main__":

    process = CrawlerProcess()

    process.crawl(XiazaiSpider)
    process.start()

    pptv_movie_w.close()
    pptv_tv_w.close()

