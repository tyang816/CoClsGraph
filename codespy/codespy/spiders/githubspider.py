import scrapy
import yaml


class GithubSpider(scrapy.Spider):
    name = 'githubspider'
    allowed_domains = ['api.github.com']
    start_urls = ['http://api.github.com/search/repositories']
    

    def start_requests(self):
        config = yaml.load('../configs/spider_config.yml', Loader=yaml.FullLoader)
        q = eval(config["q"])
        q_string = " ".join([key + ":" + value for key, value in q.items()])
        for url in self.start_urls:
            params = {
                "l": config["l"],
                "q": q_string,
                "sort": config["sort"],
                "per_page": config["per_page"],
                "page": config["page"],
            }
            print(params)
            yield scrapy.FormRequest(url, formdata=params, method="get", callback=self.parse)

    def parse(self, response):
        print(response.body)
        pass
