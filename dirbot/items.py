# from scrapy.item import Item, Field


# class Website(Item):

#     name = Field()
#     description = Field()
#     url = Field()


from scrapy.item import Item, Field


class Website(Item):

    position = Field()
    company = Field()
    positionSalaryURL = Field()
    # avgSalary = Field()
    # salaryCount = Field()
