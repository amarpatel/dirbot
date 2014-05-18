from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "positions"
    allowed_domains = ["glassdoor.com"]
    ##links for the first 7 pages (pages that contain > 100 salary reports)
    start_urls = [
        "http://www.glassdoor.com/Salary/Facebook-Software-Engineer-San-Francisco-Salaries-EJI_IE40772.0,8_KO9,26_IL.27,40_IM759.htm"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//table[@class="memberChart"]/tbody/tr[@class="dataRow"]')
        # sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()

            item['avgTotalPay'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
            # item['avgTotalPay'] = site.xpath('td[@class="mean"]').extract()
            # item['position'] = site.xpath('p/a/strong/tt[@class="i-occ"]/text()').extract()
            # item['positionSalaryURL'] = site.xpath('p/a/@href').extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
            # item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items
