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

        # Finds Total Avg Pay -- not working!!!!
            # print site.xpath('td[@class="occ"]').extract()

            # Finds Avg Salary -- works!
            if site.xpath('td[@class="occ"]/p/text()').extract()[0] == 'Salary (':
                item['avgSalary'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()

            # Finds Bonus -- works!
            if site.xpath('td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Bonuses']:
                item['bonusTotal'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()

            
            # Finds Cash Bonus -- works!
            if site.xpath('td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Cash Bonus (', u')']:
                item['cashBonus'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
            
            # Finds Stock Bonus -- works!
            if site.xpath('td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Stock Bonus (', u')']:
                item['stockBonus'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
            
            # Finds Profit Sharing -- works!
            if site.xpath('td[@class="occ"]/p[@class="indented"]/text()').extract() == [u'Profit Sharing (', u')']:
                item['profitSharing'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
            

            # if site.xpath('td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Other Pay']:
                # item['otherPay'] = site.xpath('td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
                # print: 'yup'

            # commissionsOnSales
            # tips
                
            items.append(item)

        return items

    # if x < 0:
    #      x = 0
    #      print 'Negative changed to zero'
    #  elif x == 0:
    #      print 'Zero'
    #  elif x == 1:
    #      print 'Single'
    #  else:
    #      print 'More'