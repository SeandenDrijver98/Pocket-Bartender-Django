import scrapy
from bartender_scraper.items import BartenderDrinkItem


class RecipeSpider(scrapy.Spider):
    name = "recipes"
    start_urls = ["https://www.allrecipes.com/recipes/133/drinks/cocktails/"]

    def parse(self, response, **kwargs):
        recipe = BartenderDrinkItem()
        recipe.title = response.css('h1::text').get()
        recipe.ingredients = response.css('.ingredient_list-item::text').getall()
        yield recipe
