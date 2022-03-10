import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.githubspider import GithubSpider

# 创建一个CrawlerProcess对象
process = CrawlerProcess() # 括号中可以添加参数

process.crawl(GithubSpider)
process.start()