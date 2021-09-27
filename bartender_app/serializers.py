from rest_framework import serializers
from bartender_app.models import Drink, Ingredient


class DrinkSerializer(serializers.ModelSerializer):
    instructions = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)


    class Meta:
        model = Drink
        fields = ['title', 'ingredients', 'instructions', 'description', 'image']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'title']
