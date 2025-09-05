import scrapy
from ..items import QuotesElementsDatabase4Item


class Job2Spider(scrapy.Spider):
    name = "job2"
    allowed_domains = ["remote.co"]
    start_urls = ["https://remote.co/remote-jobs/developer"]

    def parse(self, response):
        job_card = response.xpath('//div[contains(@id,"job-table-wrapper")]/div')
        for job in job_card:
            item = QuotesElementsDatabase4Item()
            item['title'] = job.xpath('.//a/span[contains(@class, "jYWVDl")]/text()').get(default='').strip()
            item['company'] = job.xpath('.//div/h3[starts-with(@id, "company-name-")]/text()').get(default='').strip()
            item['details'] = "; ".join([d.strip() for d in job.xpath('.//ul/li/text()').getall() if d.strip()])
            item['location'] = job.xpath('.//span[contains(@class, "beUnFW")]/text()').get(default='').strip()

            yield item
                

        # next page navigation
        for page in range(1, 27):  # adjust max page
            url = f"https://remote.co/remote-jobs/developer?page={page}"
            yield scrapy.Request(url, callback=self.parse)

