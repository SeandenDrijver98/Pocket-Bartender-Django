from time import sleep

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Drink, Ingredient, UserIngredient, User
from .serializers import (
    DrinkSerializer,
    IngredientSerializer,
    UserSerializer,
    UserIngredientSerializer,
)
from .filters import DrinksFilterSet


# Create your views here.
class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    filterset_class = DrinksFilterSet
    serializer_class = DrinkSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title','ingredients__title']

    def list(self, request, *args, **kwargs):
        print("here")
        sleep(10)
        return Response(data={}, status=200)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


@permission_classes([IsAuthenticated])
class UserIngredientViewset(viewsets.ModelViewSet):
    queryset = UserIngredient.objects.all()
    serializer_class = UserIngredientSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by(
            "-ingredient__title"
        )


# Register API
class UserAPI(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": serializer.data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )
