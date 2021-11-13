from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Drink, Ingredient
from .serializers import DrinkSerializer, IngredientSerializer
from .filters import DrinksFilterSet
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.
class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    filterset_class = DrinksFilterSet
    serializer_class = DrinkSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title','ingredients__title']


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


def signup_view(request):
    username = request.POST["email_address"]
    password = request.POST["password"]
    user = User.objects.create_user(username=username, password=password)

    if user:
        login(request, user)


def login_view(request):
    username = request.POST["email_address"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        print("logged in")
        return redirect("drink-list")
    else:
        return


def logout_view(request):
    logout(request)
