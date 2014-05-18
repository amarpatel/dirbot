from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "glassdoor"
    allowed_domains = ["glassdoor.com"]
    ##links for the first 7 pages (pages that contain > 100 salary reports)
    start_urls = [
        "http://www.glassdoor.com/Salaries/software-engineer-salary-SRCH_KO0,17.htm",
        'http://www.glassdoor.com/Salaries/software-engineer-salaries-SRCH_KO0,17_IP2.htm',
        'http://www.glassdoor.com/Salaries/software-engineer-pay-SRCH_KO0,17_IP3.htm',
        'http://www.glassdoor.com/Salaries/software-engineer-wages-SRCH_KO0,17_IP4.htm',
        'http://www.glassdoor.com/Salaries/average-software-engineer-salary-SRCH_KO8,25_IP5.htm',
        'http://www.glassdoor.com/Salaries/average-software-engineer-salaries-SRCH_KO8,25_IP6.htm',
        'http://www.glassdoor.com/Salaries/average-software-engineer-salary-SRCH_KO8,25_IP7.htm'
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//tr[@class="dataRow first"]/td[@class="occ"]')
        # sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()

            # I'm in the table now...
                #grab first td (title, co, sal#)
                    #title: td w/ class 'occ'  
            item['company'] = site.xpath('p/a/tt[@class="i-emp"]/text()').extract()
            item['position'] = site.xpath('p/a/strong/tt[@class="i-occ"]/text()').extract()
            item['positionSalaryURL'] = site.xpath('p/a/@href').extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
            # item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items
