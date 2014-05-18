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
        sites = sel.xpath('//table[@class="memberChart"]/tbody')
        # sites = sel.xpath('//table[@class="memberChart"]/tbody/tr[@class="dataRow"]')
        # sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()

            # Finds Total Avg Pay -- works!
            if site.xpath('tr[@class="dataRow titleRow first"]/td[@class="occ"]/p/strong/strong/text()').extract() == [u'Total Pay']:
                item['avgTotalPay'] = site.xpath('tr[@class="dataRow titleRow first"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()

            # Finds Avg Salary -- works!
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/text()').extract()[0] == 'Salary (':
                item['avgSalary'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()

            # Finds Bonus -- works!
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Bonuses']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['bonusTotal'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['otherPay'] = 0

            # Finds Cash Bonus
            print site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() [0]
            # if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Cash Bonus (', u')']:
                # if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                #     item['cashBonus'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                # else:
                #     item['cashBonus'] = 0

            # Finds Stock Bonus
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Stock Bonus (', u')']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['stockBonus'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['stockBonus'] = 0
            
            # Finds Profit Sharing
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Profit Sharing (', u')']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['profitSharing'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['profitSharing'] = 0

            # Other Pay -- works!
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Other Pay']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['otherPay'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['otherPay'] = 0

            # Commisions On Sales
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Commissions on Sales (', u')']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['commissionsOnSales'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['commissionsOnSales'] = 0
                    
            # Tips
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Tips (', u')']:
                if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
                    item['tips'] = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                else:
                    item['tips'] = 0           


            items.append(item)

        return items





