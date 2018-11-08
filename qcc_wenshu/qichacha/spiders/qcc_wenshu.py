# -*- coding: utf-8 -*-
import scrapy
from qichacha.items import WenshuItem
from qichacha.settings import COOKIES
import urllib.parse
import re
import chardet
class QccWenshuSpider(scrapy.Spider):
    name = 'qcc_wenshu'
    start_urls = ['https://www.qichacha.com/search?key=']
    page = 1

    def start_requests(self):
        f = open('company_list.txt', 'r', encoding='utf-8')
        for link in f:
            company = urllib.parse.quote(link).replace('\n', '')
            url = self.start_urls[0] + company
            check_name = link

            yield scrapy.Request(url, cookies=COOKIES, callback=self.parse,meta={'check_name':check_name},encoding='utf-8')

    def parse(self,response):
        check_ming = response.meta['check_name']
        link = response.xpath('//tbody/tr[1]/td[2]/a/@href').extract_first()
        detail_link = response.urljoin(link)
        yield scrapy.Request(detail_link,cookies=COOKIES,callback=self.parse_wenshu,meta={'mingz':check_ming},encoding='utf-8')

    def parse_wenshu(self, response):
        #公司名
        name = response.xpath('//div[@class="row title"]/h1/text()').extract_first()
        #搜索公司名（查询的某些公司可能使用的是曾用名）
        search_name = response.meta['mingz']

        #裁判文书
        #https://www.qichacha.com/company_getinfos?unique=576c21e3468a6b178bbf291e4820e896&companyname=%E5%8C%97%E4%BA%AC%E7%99%BE%E5%BA%A6%E7%BD%91%E8%AE%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&tab=susong&box=wenshu&p=1
        unique_str = response.url.split('/')[-1]
        unique = re.findall('firm_(.*).html', unique_str)[-1]
        company_name = urllib.parse.quote(name)
        wenshu = 'https://www.qichacha.com/company_getinfos?unique=' + unique + '&companyname=' + company_name + '&tab=susong&box=wenshu&p='
        wenshu_link = wenshu + str(self.page)
        yield scrapy.Request(wenshu_link,cookies=COOKIES,callback=self.parse_detail,encoding='utf-8',meta={'search_name':search_name,'name':name})

    def parse_detail(self,response):
        data = response.xpath('//table/tr')
        if data:
            search_name = response.meta['search_name']
            name = response.meta['name']

            bigtag = response.xpath('//table[@class="ntable ntable-odd"]/tr[position()>1]')
            for tag in bigtag:
                subitem = {}
                subitem['search_name'] = search_name
                subitem['name'] = name

                case_name = tag.xpath('.//td[2]/a/text()').extract_first()
                subitem['case_name'] = case_name if case_name else '暂无信息'

                cause = tag.xpath('.//td[3]/text()').extract_first()
                subitem['cause'] = cause if cause else '暂无信息'

                release_time = tag.xpath('.//td[4]/text()').extract_first()
                subitem['release_time'] = release_time if release_time else '暂无信息'

                case_num = tag.xpath('.//td[5]/text()').extract_first()
                subitem['case_num'] = case_num if case_num else '暂无信息'

                littletag = tag.xpath('.//td[6]')
                case_status = littletag.xpath('string(.)').extract_first()
                subitem['case_status'] = case_status if case_status else '暂无信息'

                executive_court = tag.xpath('.//td[7]/text()').extract_first()
                subitem['executive_court'] = executive_court if executive_court else '暂无信息'

                case_detail = tag.xpath('.//td[2]/a/@href').extract()
                if case_detail:
                    det_link = 'https://www.qichacha.com' + case_detail[0]
                    yield scrapy.Request(det_link,callback=self.content_parse,meta={'basic':subitem},encoding='utf-8')

            page_num = response.xpath('//ul[@class="pagination"]/li/a/text()').extract()
            com_set = []
            for j in page_num:
                ye = re.findall('\d+',j)
                if ye != []:
                    com_set.append(ye[0])
            page1 = com_set[-1] if page_num else 1
            pattern = '(https:.*?p=)\d+'
            next_links = re.findall(pattern,response.url)
            next_link = next_links[0]
            for i in range(2,int(page1)+1):
                next_url = next_link + str(i)
                yield scrapy.Request(next_url,callback=self.parse_detail,encoding='utf-8')

    def content_parse(self,response):
        item = WenshuItem()
        basic_info = response.meta['basic']

        xiangqing = response.xpath('//div[@class="col-md-9"]/section[@id="searchlist"]/div[@id="wsview"]')
        content_view = xiangqing.xpath('string(.)').extract_first().replace('\n',' ').replace('\u3000','').replace('\xa0','').replace("'","").replace('"','')

        item['search_name'] = basic_info['search_name']
        item['name'] = basic_info['name']
        item['case_name'] = basic_info['case_name']
        item['cause'] = basic_info['cause']
        item['release_time'] = basic_info['release_time']
        item['case_num'] = basic_info['case_num']
        item['case_status'] = basic_info['case_status']
        item['executive_court'] = basic_info['executive_court']
        item['wsview'] = content_view
        yield item






