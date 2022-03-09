import scrapy


class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
    allowed_domains = ['api.github.com']
    start_urls = ['http://api.github.com/']

    def parse(self, response):
        pass
