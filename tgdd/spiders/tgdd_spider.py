# -*- coding: utf-8 -*-
import scrapy
import os


CATEGORIES = ['dtdd', 'may-tinh-bang', 'laptop', 'dong-ho-thong-minh', 'dong-ho-deo-tay']

CATEGORIES_CODE = {
    'dtdd': '42',
    'may-tinh-bang': 'may-tinh-bang',
    'laptop': '44',
    'dong-ho-thong-minh': '7077',
    'dong-ho-deo-tay': '7264'
}

# CATEGORIES_NAME = {
#     '42': 'dtdd',
#     '522': 'may-tinh-bang',
#     '44': 'laptop',
#     '7077': 'dong-ho-thong-minh',
#     '7264': 'dong-ho-deo-tay'
# }

class Tgdd(scrapy.Spider):
    name = 'tgdd'
    url = 'https://www.thegioididong.com'
    start_urls = []

    def __init__(self, category=None, *args, **kwargs):
        super(Tgdd, self).__init__(*args, **kwargs)
        if category is not None:
            if not os.path.exists('./%s' % category):
                os.makedirs('./%s' % category)
            link = self.url + '/' + category
            self.start_urls.append(link)
        else:
            for category in CATEGORIES:
                if not os.path.exists('./%s' % category):
                    os.makedirs('./%s' % category)
                link = self.url + '/' + category
                self.start_urls.append(link)

    def parse(self, response):
        text = response.css('a.viewmore::text').get()
        url = 'https://www.thegioididong.com/aj/CategoryV5/Product'
        print('--------------------------------')
        items = response.css('ul.homeproduct  li  a::attr(href)').extract()
        for item in items:
            item_link = self.url + item
            yield scrapy.Request(url=item_link, callback=parse_item)
            # print(item_link)

        if text is not None:
            category = self.get_category_code(response)
            page_index = self.get_page_index(response)
            print(page_index)
            print(category)
            frm_data = {
                'Category': str(category),
                'Manufacture': '0',
                'PriceRange': '0',
                'Feature': '0',
                'Property': '0',
                'OrderBy': '0',
                'PageSize': '30',
                'PageIndex': str(page_index + 1),
                'Others': '',
                'ClearCache': '0'
            }
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=frm_data, dont_filter=True)

    @staticmethod
    def get_page_index(response):
        form_data = response.request.body.decode("utf-8")
        if form_data is '':
            return 0
        else:
            form_data = form_data.split("&")
            page_index = int(form_data[7].split("=")[1])
            return page_index

    @staticmethod
    def get_category_code(response):
        form_data = response.request.body.decode("utf-8")
        if form_data is '':
            url = response.request.url.split("/")
            category_code = CATEGORIES_CODE[url[3]]
            return category_code
        else:
            form_data = form_data.split("&")
            category_code = form_data[0].split("=")[1]
            return category_code

    def parse_item(self, response):
        name = response.css('body > section > div.rowtop > h1::text').get()
        print(name)



    # @staticmethod
    # def get_page_index(items_left):
    #     page_index = ceil(items_left / 30)
    #     return int(page_index)


# @staticmethod
# def get_page_num(response):
#     page_num = response.request.url[-1]
#     if page_num.isdigit():
#         return page_num
#     else:
#         return '0'
# if text is None:
#     url = self.get_url_full(text.split(" ")[2], response.request.url)
#     yield scrapy.Request(url, callback=self.parse)
# else:
#     for item in response.css('ul.homeproduct  li  a::attr(href)').extract():
#         pass

# # Get url of full item page
# def get_url_full(self, current_url, items_left):
#     num = int((int(items_left) / 30)) + 1
#     full_url = current_url + '#i:%d' % num
#     return full_url

def parse_item(self, response):
    pass
