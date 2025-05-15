# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prod_name = scrapy.Field()
    brand = scrapy.Field()
    battery = scrapy.Field()
    os = scrapy.Field()
    cpu = scrapy.Field()
    gpu = scrapy.Field()
    cost = scrapy.Field()
    weight = scrapy.Field()
    ram = scrapy.Field()
    screen_size = scrapy.Field()
    screen_fresh_rate = scrapy.Field()
    screen_resolution = scrapy.Field()
    battery_capacity = scrapy.Field()

