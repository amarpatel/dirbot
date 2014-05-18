from scrapy.item import Item, Field


class Website(Item):

    position = Field()
    company = Field()
    positionSalaryURL = Field()
    salaryCount = Field()