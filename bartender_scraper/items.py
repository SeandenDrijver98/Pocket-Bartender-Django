# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from bartender_app.models import Drink, DrinkIngredient


class BartenderDrinkItem(DjangoItem):
    django_model = Drink


class BartenderIngredientItem(DjangoItem):
    django_model = DrinkIngredient


class BartenderScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
