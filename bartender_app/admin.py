from django.contrib import admin
from .models import Ingredient, Drink, DrinkIngredient, DrinkInstruction, UserIngredient

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Drink)
admin.site.register(DrinkIngredient)
admin.site.register(DrinkInstruction)
admin.site.register(UserIngredient)
