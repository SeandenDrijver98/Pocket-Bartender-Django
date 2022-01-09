from django.contrib import admin
from .models import Ingredient, Drink, DrinkIngredient, UserIngredient, Category

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(DrinkIngredient)
admin.site.register(UserIngredient)
admin.site.register(Category)


class DrinkIngredientInline(admin.TabularInline):
    model = DrinkIngredient


class DrinkAdmin(admin.ModelAdmin):
    inlines = [DrinkIngredientInline]


admin.site.register(Drink, DrinkAdmin)
