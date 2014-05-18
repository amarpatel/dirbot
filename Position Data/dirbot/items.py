from scrapy.item import Item, Field


class Website(Item):

    avgTotalPay = Field()
    avgSalary = Field()
    bonusTotal = Field()
    cashBonus = Field()
    stockBonus = Field()
    profitSharing = Field()
    otherPay = Field()
    commissionsOnSales = Field()
    tips = Field()
