import django_filters
from .models import Drink,Ingredient,UserIngredient


class DrinksFilterSet(django_filters.FilterSet):
        title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')

        class Meta:
            model = Drink
            fields = ['title']


class IngredientsFilterSet(django_filters.FilterSet):
    in_stock = django_filters.BooleanFilter(method='in_stock_filter')

    class Meta:
        model = Ingredient
        fields = ['title']

    def in_stock_filter(self, queryset, name, value):
        print('name', name)
        print('value', value)
        print('queryset', queryset)

        return queryset
