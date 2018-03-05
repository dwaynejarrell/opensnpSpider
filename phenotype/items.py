import scrapy
from collections import defaultdict


class UserItem(scrapy.Item):
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        self._values[key] = value
    #
    # id = scrapy.Field()
    # # variations = scrapy.Field()
    # variations = defaultdict(scrapy.Field)
