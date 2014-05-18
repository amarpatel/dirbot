from scrapy.item import Item, Field


class Website(Item):

    company = Field()
    companyRating = Field()
    companyRatingNum = Field()
    urlAndCompany = Field()
    avgTotalPay = Field()
    avgSalary = Field()
    bonusTotal = Field()
    cashBonus = Field()
    stockBonus = Field()
    profitSharing = Field()
    otherPay = Field()
    commissionsOnSales = Field()
    tips = Field()
