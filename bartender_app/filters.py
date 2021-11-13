import django_filters
from .models import Drink, Ingredient, UserIngredient, DrinkIngredient
from django.db.models import Count, Q, ExpressionWrapper, F, FloatField


class DrinksFilterSet(django_filters.FilterSet):
    # title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')
    # ingredient = django_filters.CharFilter(field_name="ingredients__title", lookup_expr='icontains')
    ordering = django_filters.CharFilter(field_name="stock", method="ordering_filter")
    # spirit = django_filters.C

    class Meta:
        model = Drink
        fields = ["title"]

    def ordering_filter(self, queryset, name, value):
        if value == "stock":
            """
            SELECT COUNT(*)  num_ingredients, d.title FROM bartender_app_useringredient ui
            LEFT JOIN bartender_app_drinkingredient di on ui.ingredient_id == di.ingredient_id
            LEFT JOIN bartender_app_drink d on d.id == di.drink_id
            where user_id == 1
            group by di.drink_id
            """
            user = self.request.user
            # Order by number of owned ingredients
            # return queryset.all().annotate(ingredient_count=Count('ingredients__ingredient',filter=Q(ingredients__ingredient__id__in=UserIngredient.objects.filter(user_id=1).values_list('ingredient_id',flat=True)))).order_by('ingredient_count')

            # Order by lowest percentage of missing ingredients
            return (
                queryset.all()
                .annotate(
                    ingredient_stock_count=Count(
                        "ingredients__ingredient",
                        filter=Q(
                            ingredients__ingredient__id__in=UserIngredient.objects.filter(
                                user_id=1
                            ).values_list(
                                "ingredient_id", flat=True
                            )
                        ),
                    ),
                    ingredient_count=Count("ingredients__ingredient"),
                    ingredient_stock_ratio=ExpressionWrapper(
                        F("ingredient_stock_count") / F("ingredient_count"),
                        output_field=FloatField(),
                    ),
                )
                .order_by("ingredient_count")
            )


class IngredientsFilterSet(django_filters.FilterSet):
    in_stock = django_filters.BooleanFilter(method="in_stock_filter")

    class Meta:
        model = Ingredient
        fields = ["title"]

    def in_stock_filter(self, queryset, name, value):
        user = self.request.user
        return queryset.filter(id__in=(UserIngredient.objects.filter(user_id="1")))
