from rest_framework import routers
from django.urls import path, include
from .views import DrinkViewSet, IngredientViewSet, UserAPI, UserIngredientViewset

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"drinks", DrinkViewSet)
router.register(r"ingredients", IngredientViewSet)
router.register(r"my-ingredients", UserIngredientViewset)

urlpatterns = [
    path("signup/", UserAPI.as_view(), name="signup"),
    path("", include(router.urls)),
]
