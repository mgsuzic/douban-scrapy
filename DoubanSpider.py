#coding: utf-8

import sys

class DoubanSpider(scrapy.Spider):
    # 必须定义
    name = "douban"
    # 初始urls
    start_urls = ["https://book.douban.com/subject/1676611/",
            "https://read.douban.com/ebook/24791669/"]

    # 默认response处理函数
    def parse(self, response):
        # 把结果写到文件中
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
		print "xxx"
		
		
if __name__ == "__main__":
	pass