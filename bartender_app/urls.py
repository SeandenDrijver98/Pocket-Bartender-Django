from rest_framework import routers
from django.urls import path, include
from .views import DrinkViewSet, IngredientViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"drinks", DrinkViewSet)
router.register(r"ingredients", IngredientViewSet)
router.register(r"ingredient_stock", DrinkViewSet)

urlpatterns = [path("", include(router.urls))]
