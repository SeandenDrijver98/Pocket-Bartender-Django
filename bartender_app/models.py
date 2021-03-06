from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Glass(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="media/glasses")

    def __str__(self):
        return f"{self.title}"


class Ingredient(models.Model):
    INGREDIENT_TYPE_CHOICES = [
        ("spirit", "SPIRIT"),
        ("mixer", "MIXER"),
        ("garnish", "GARNISH"),
    ]
    title = models.CharField(max_length=255)
    type = models.CharField(choices=INGREDIENT_TYPE_CHOICES, max_length=15)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Drink(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="media/drinks")
    instructions = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    method = models.TextField(
        choices=[("shaken", "Shaken"), ("stirred", "Stirred")], null=True
    )
    glass = models.ForeignKey(Glass, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class DrinkIngredient(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="in_drinks"
    )
    quantity_needed = models.FloatField(default=0)
    measurement = models.CharField(max_length=255, default="", blank=True)
    optional = models.BooleanField(default=False)
    drink = models.ForeignKey(
        Drink, related_name="ingredients", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return f"{self.quantity_needed} {self.measurement} {self.ingredient}"


class UserIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="available_ingredients"
    )

    def __str__(self):
        return f"{self.ingredient} - {self.user.username}"
