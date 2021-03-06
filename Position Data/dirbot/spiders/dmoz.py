from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "positions"
    allowed_domains = ["glassdoor.com"]
    ##links for the first 7 pages (pages that contain > 100 salary reports)
    start_urls = [
        'http://www.glassdoor.com/Salary/iTech-US-Software-Engineer-Salaries-E266493_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/Keane-Software-Engineer-Salaries-E1563_D_KO6,23.htm',
        'http://www.glassdoor.com/Salary/Brocade-Communications-Software-Engineer-Salaries-E9183_D_KO23,40.htm',
        'http://www.glassdoor.com/Salary/EMC-Software-Engineer-Salaries-E219_D_KO4,21.htm',
        'http://www.glassdoor.com/Salary/Mahindra-Satyam-Software-Engineer-Salaries-E241456_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/RJT-Compuquest-Software-Engineer-Salaries-E249174_D_KO15,32.htm',
        'http://www.glassdoor.com/Salary/Wisdom-Infotech-Software-Engineer-Salaries-E195228_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/Fujitsu-Consulting-Software-Engineer-Salaries-E362490_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/Logistic-Solutions-Inc-Software-Engineer-Salaries-E195640_D_KO23,40.htm',
        'http://www.glassdoor.com/Salary/IndSoft-Software-Engineer-Salaries-E366008_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Software-Paradigms-Software-Engineer-Salaries-E136631_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/IntraEdge-Software-Engineer-Salaries-E269780_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Orpine-Software-Engineer-Salaries-E270146_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Garmin-Software-Engineer-Salaries-E12667_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Symantec-Software-Engineer-Salaries-E1931_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/American-Unit-Software-Engineer-Salaries-E267173_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Everest-Computers-Software-Engineer-Salaries-E271555_D_KO18,35.htm',
        'http://www.glassdoor.com/Salary/Sree-Infotech-Software-Engineer-Salaries-E282538_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/iconsoft-Software-Engineer-Salaries-E155359_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/Horizon-Computer-Services-Software-Engineer-Salaries-E279409_D_KO26,43.htm',
        'http://www.glassdoor.com/Salary/Google-Software-Engineer-Salaries-E9079_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Fujitsu-Software-Engineer-Salaries-E3524_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Intel-Corporation-Software-Engineer-Salaries-E1519_D_KO18,35.htm',
        'http://www.glassdoor.com/Salary/Qualcomm-Software-Engineer-Salaries-E640_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/Cisco-Systems-Software-Engineer-Salaries-E1425_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/American-Solutions-Inc-Software-Engineer-Salaries-E228267_D_KO23,40.htm',
        'http://www.glassdoor.com/Salary/Yahoo-Software-Engineer-Salaries-E5807_D_KO6,23.htm',
        'http://www.glassdoor.com/Salary/Fujitsu-America-Software-Engineer-Salaries-E354088_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/Facebook-Software-Engineer-Salaries-E40772_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/MphasiS-Software-Engineer-Salaries-E29275_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/IBM-Software-Engineer-Salaries-E354_D_KO4,21.htm',
        'http://www.glassdoor.com/Salary/Yash-and-Lujan-Consulting-Software-Engineer-Salaries-E290731_D_KO26,43.htm',
        'http://www.glassdoor.com/Salary/Cerner-Software-Engineer-Salaries-E1242_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Motorola-Mobility-Software-Engineer-Salaries-E451_D_KO18,35.htm',
        'http://www.glassdoor.com/Salary/Mastech-Software-Engineer-Salaries-E32469_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Oracle-Software-Engineer-Salaries-E1737_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Apple-Software-Engineer-Salaries-E1138_D_KO6,23.htm',
        'http://www.glassdoor.com/Salary/System-Soft-Technologies-Software-Engineer-Salaries-E260662_D_KO25,42.htm',
        'http://www.glassdoor.com/Salary/Hitachi-Consulting-Software-Engineer-Salaries-E28435_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/Verizon-Software-Engineer-Salaries-E89_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Frontier-Technologies-Software-Engineer-Salaries-E368788_D_KO22,39.htm',
        'http://www.glassdoor.com/Salary/Horizon-International-TRD-Software-Engineer-Salaries-E262730_D_KO26,43.htm',
        'http://www.glassdoor.com/Salary/OTIS-Information-Technologies-Software-Engineer-Salaries-E278390_D_KO30,47.htm',
        'http://www.glassdoor.com/Salary/Triune-Technologies-Software-Engineer-Salaries-E266735_D_KO20,37.htm',
        'http://www.glassdoor.com/Salary/Relycom-Software-Engineer-Salaries-E375325_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Talented-IT-Software-Engineer-Salaries-E375888_D_KO12,29.htm',
        'http://www.glassdoor.com/Salary/Adaequare-Software-Engineer-Salaries-E264794_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Onward-Technologies-Inc-Software-Engineer-Salaries-E101060_D_KO24,41.htm',
        'http://www.glassdoor.com/Salary/Arista-Networks-Software-Engineer-Salaries-E295128_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/RapidIT-Software-Engineer-Salaries-E268677_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Datametrics-Software-Systems-Software-Engineer-Salaries-E375342_D_KO29,46.htm',
        'http://www.glassdoor.com/Salary/Thomson-Reuters-Software-Engineer-Salaries-E100303_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/NeST-Technologies-Software-Engineer-Salaries-E37580_D_KO18,35.htm',
        'http://www.glassdoor.com/Salary/Infowave-Systems-Software-Engineer-Salaries-E292301_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/KLA-Tencor-Software-Engineer-Salaries-E1557_D_KO11,28.htm',
        'http://www.glassdoor.com/Salary/Mindlance-Software-Engineer-Salaries-E249667_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Promatrix-Software-Engineer-Salaries-E608005_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Alindus-Software-Engineer-Salaries-E423532_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Bijjam-Information-Technologies-Software-Engineer-Salaries-E261772_D_KO32,49.htm',
        'http://www.glassdoor.com/Salary/GE-Healthcare-Software-Engineer-Salaries-E4112_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Inek-Technologies-Software-Engineer-Salaries-E254424_D_KO18,35.htm',
        'http://www.glassdoor.com/Salary/ISR-INFO-WAY-Software-Engineer-Salaries-E278711_D_KO13,30.htm',
        'http://www.glassdoor.com/Salary/LinkedIn-Software-Engineer-Salaries-E34865_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/FactSet-Software-Engineer-Salaries-E6066_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Intuit-Software-Engineer-Salaries-E2293_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Tavant-Technologies-Software-Engineer-Salaries-E151574_D_KO20,37.htm',
        'http://www.glassdoor.com/Salary/Infovision-Software-Engineer-Salaries-E15675_D_KO11,28.htm',
        'http://www.glassdoor.com/Salary/Covansys-Software-Engineer-Salaries-E5310_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/Tata-Consultancy-Services-Software-Engineer-Salaries-E13461_D_KO26,43.htm',
        'http://www.glassdoor.com/Salary/Smart-Insight-Software-Engineer-Salaries-E375881_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Scandent-Group-Software-Engineer-Salaries-E421435_D_KO15,32.htm',
        'http://www.glassdoor.com/Salary/MicroStrategy-Software-Engineer-Salaries-E8018_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/e-Business-Intl-Software-Engineer-Salaries-E261562_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/Rockwell-Collins-Software-Engineer-Salaries-E13435_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/Lockheed-Martin-Software-Engineer-Salaries-E404_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/OpenLogix-Corpration-Software-Engineer-Salaries-E271913_D_KO21,38.htm',
        'http://www.glassdoor.com/Salary/Trinus-Corporation-Software-Engineer-Salaries-E104502_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/NVIDIA-Software-Engineer-Salaries-E7633_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/Motorola-Solutions-Software-Engineer-Salaries-E427189_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/Twitter-Software-Engineer-Salaries-E100569_D_KO8,25.htm',
        'http://www.glassdoor.com/Hourly-Pay/Alindus-Software-Engineer-Hourly-Pay-E423532_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Zynga-Software-Engineer-Salaries-E243552_D_KO6,23.htm',
        'http://www.glassdoor.com/Salary/Trinuc-Software-Engineer-Salaries-E267308_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/CGI-Group-Software-Engineer-Salaries-E8452_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Tech-Mahindra-Software-Engineer-Salaries-E135932_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Sierra-Atlantic-Software-Engineer-Salaries-E22640_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/InfoMet-Software-Engineer-Salaries-E375670_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Apex-Technology-Systems-Software-Engineer-Salaries-E154815_D_KO24,41.htm',
        'http://www.glassdoor.com/Salary/VTEKH-Software-Engineer-Salaries-E375554_D_KO6,23.htm',
        'http://www.glassdoor.com/Salary/Aptiva-Software-Engineer-Salaries-E378332_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/IAC-Search-and-Media-Software-Engineer-Salaries-E294228_D_KO21,38.htm',
        'http://www.glassdoor.com/Salary/MathWorks-Software-Engineer-Salaries-E17117_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Infor-Global-Software-Engineer-Salaries-E15375_D_KO13,30.htm',
        'http://www.glassdoor.com/Salary/Perot-Systems-Software-Engineer-Salaries-E3327_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/TechAspect-Software-Engineer-Salaries-E271085_D_KO11,28.htm',
        'http://www.glassdoor.com/Salary/REI-Systems-Software-Engineer-Salaries-E14097_D_KO12,29.htm',
        'http://www.glassdoor.com/Salary/DivIHN-Integration-Software-Engineer-Salaries-E114001_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/RDG-Technologies-Software-Engineer-Salaries-E273266_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/People-Incorporated-Software-Engineer-Salaries-E139727_D_KO20,37.htm',
        'http://www.glassdoor.com/Salary/National-Instruments-Software-Engineer-Salaries-E4030_D_KO21,38.htm',
        'http://www.glassdoor.com/Hourly-Pay/Mastech-Software-Engineer-Hourly-Pay-E32469_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/eBay-Inc-Software-Engineer-Salaries-E7853_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/TechDemocracy-Software-Engineer-Salaries-E355475_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Frontline-Consulting-Services-Software-Engineer-Salaries-E326148_D_KO30,47.htm',
        'http://www.glassdoor.com/Hourly-Pay/Axiom-Sources-Software-Engineer-Hourly-Pay-E269264_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Saven-Technologies-Software-Engineer-Salaries-E133995_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/HTC-Global-Services-Software-Engineer-Salaries-E14779_D_KO20,37.htm',
        'http://www.glassdoor.com/Salary/Sasken-Software-Engineer-Salaries-E220768_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/UST-Global-Software-Engineer-Salaries-E155577_D_KO11,28.htm',
        'http://www.glassdoor.com/Salary/Logic-Planet-Software-Engineer-Salaries-E279609_D_KO13,30.htm',
        'http://www.glassdoor.com/Salary/Anira-Solutions-Software-Engineer-Salaries-E278405_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/PayPal-Software-Engineer-Salaries-E9848_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/I-and-I-Software-Software-Engineer-Salaries-E269981_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/Mitchell-Martin-Software-Engineer-Salaries-E263872_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/Everest-Business-Solutions-Software-Engineer-Salaries-E117234_D_KO27,44.htm',
        'http://www.glassdoor.com/Salary/Hewlett-Packard-Software-Engineer-Salaries-E327_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/HCL-Technologies-Software-Engineer-Salaries-E553909_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/MNCL-Software-Engineer-Salaries-E375300_D_KO5,22.htm',
        'http://www.glassdoor.com/Salary/Ericsson-Worldwide-Software-Engineer-Salaries-E3472_D_KO19,36.htm',
        'http://www.glassdoor.com/Salary/Itwotech-Software-Engineer-Salaries-E375262_D_KO9,26.htm',
        'http://www.glassdoor.com/Salary/IT-People-Software-Engineer-Salaries-E274233_D_KO10,27.htm',
        'http://www.glassdoor.com/Salary/Amensys-Software-Engineer-Salaries-E280221_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Reasonsoft-Software-Engineer-Salaries-E267456_D_KO11,28.htm',
        'http://www.glassdoor.com/Salary/CA-Technologies-Software-Engineer-Salaries-E167_D_KO16,33.htm',
        'http://www.glassdoor.com/Salary/Multivision-Illinois-Software-Engineer-Salaries-E230135_D_KO21,38.htm',
        'http://www.glassdoor.com/Salary/Semantic-Space-Software-Engineer-Salaries-E311262_D_KO15,32.htm',
        'http://www.glassdoor.com/Salary/International-Game-Technology-Software-Engineer-Salaries-E1527_D_KO30,47.htm',
        'http://www.glassdoor.com/Salary/Moxie-Systems-Software-Engineer-Salaries-E375237_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Nihaki-Systems-Software-Engineer-Salaries-E266408_D_KO15,32.htm',
        'http://www.glassdoor.com/Salary/Enrich-Software-Engineer-Salaries-E268079_D_KO7,24.htm',
        'http://www.glassdoor.com/Salary/E-Infotek-Solutions-Software-Engineer-Salaries-E270155_D_KO20,37.htm',
        'http://www.glassdoor.com/Salary/Mascon-Global-Software-Engineer-Salaries-E14201_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Qualcomm-Atheros-Software-Engineer-Salaries-E13698_D_KO17,34.htm',
        'http://www.glassdoor.com/Salary/Imetris-Software-Engineer-Salaries-E259404_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/CybeCys-Software-Engineer-Salaries-E375674_D_KO8,25.htm',
        'http://www.glassdoor.com/Salary/Surya-Systems-Software-Engineer-Salaries-E269655_D_KO14,31.htm',
        'http://www.glassdoor.com/Salary/Citrix-Systems-Software-Engineer-Salaries-E5432_D_KO15,32.htm',
        'http://www.glassdoor.com/Salary/USM-Business-Systems-Software-Engineer-Salaries-E195193_D_KO21,38.htm',
        'http://www.glassdoor.com/Salary/Serene-Corporation-Software-Engineer-Salaries-E213793_D_KO19,36.htm',
        'http://www.glassdoor.com/Hourly-Pay/AdeptMax-Software-Engineer-Hourly-Pay-E262253_D_KO9,26.htm'
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        # sites = sel.xpath('//div[@class="pageContentWrapper"]')
        sites = sel.xpath('//table[@class="memberChart"]/tbody')
        items = []
        # tablePath = '/div[@id="PageContent"]/div[@id="PageBodyContents"]/div[@class="pageInsideContent cf"]/div[@id="EI-Srch"]/div[@id="EI"]/div[@id="EISalaries"]/div[@id="SalaryJobSummary"]/div/div[@id="MainCol"]/div/table[@class="memberChart"]/tbody/'

        for site in sites:

            # print 'look here'
            # print self
            # print response
            # print sel

            item = Website()
            # tablePath = '/div[@id="PageContent"]/div[@class="meat"]/div[@class="pageInsideContent"]/div[@class="ajaxContent"]/div[@id="EI"]/div[@id="EISalaries"]/div[@id="SalaryJobSummary"]/div[@class="grid"]/div[@id="MainCol"]/div[@class="SalaryChart"]/table/tbody/'
            # tablePath = '//table[@class="memberChart"]/tbody'
            # scrapy crawl positions -o items.json -t json

            # Finds Total Avg Pay -- works
            if site.xpath('tr[@class="dataRow titleRow first"]/td[@class="occ"]/p/strong/strong/text()').extract() == [u'Total Pay']:
                avgTotalPay = site.xpath('tr[@class="dataRow titleRow first"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[0]

            # Finds Avg Salary -- works
            if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/text()').extract()[0] == 'Salary (':
                avgSalary = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[0]

            # # Finds Bonus -- works
            # if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Bonuses']:
            #     if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
            #         bonusTotal = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[0]
            #     else:
            #         bonusTotal = 0

            # Finds Cash Bonus -- works
            if u'Cash Bonus (' in site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract():
                try:
                    cashBonus = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[0]
                except IndexError:
                    cashBonus = 0

            # Finds Stock Bonus -- works
            if u'Stock Bonus (' in site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract():
                try:
                    stockBonus = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[1]
                except IndexError:
                    stockBonus = 0
            
            # Finds Profit Sharing -- works
            if u'Profit Sharing (' in site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract():
                try:
                    profitSharing = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[2]
                except IndexError:
                    profitSharing = 0

            # # Other Pay -- works
            # if site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p/span[@class="toggle expanded"]/a/text()').extract() == [u'Other Pay']:
            #     if site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/text()').extract() != [u'n/a']:
            #         otherPay = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()
            #     else:
            #         otherPay = 0

            # Commisions On Sales -- works
            if u'Commissions on Sales (' in site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract():
                try:
                    commissionsOnSales = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[0]
                except IndexError:
                    commissionsOnSales = 0
                    
            # Tips -- works
            if u'Tips (' in site.xpath('tr[@class="dataRow"]/td[@class="occ"]/p[@class="indented"]/text()').extract():
                try:
                    tips = site.xpath('tr[@class="dataRow"]/td[@class="mean"]/span[@class="minor"]/tt[@class="notranslate"]/text()').extract()[1]
                except IndexError:
                    tips = 0


            # declare variable for intial table location
            # find company name
            # find company rating
            # find number of company ratings

                # item['company'] = company
                # item['companyRating'] = companyRating
                # item['companyRatingNum'] = companyRatingNum
                item['urlAndCompany'] = response
                item['avgTotalPay'] = avgTotalPay
                item['avgSalary'] = avgSalary
                # item['bonusTotal'] = bonusTotal
                item['cashBonus'] = cashBonus
                item['stockBonus'] = stockBonus
                item['profitSharing'] = profitSharing
                # item['otherPay'] = otherPay
                item['commissionsOnSales'] = commissionsOnSales
                item['tips'] = tips


            items.append(item)

        return items





