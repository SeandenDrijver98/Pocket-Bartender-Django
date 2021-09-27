from django.shortcuts import render
from rest_framework import viewsets
from .models import Drink, Ingredient
from .serializers import DrinkSerializer, IngredientSerializer
from .filters import DrinksFilterSet


# Create your views here.
class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    filterset_class = DrinksFilterSet

    serializer_class = DrinkSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
