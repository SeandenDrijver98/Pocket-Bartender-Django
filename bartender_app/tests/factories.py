from factory import LazyAttribute, SubFactory, post_generation
from factory.django import DjangoModelFactory
from random import randint
import mimesis

from ..models import Ingredient

fake = mimesis.Generic('en')


class IngredientFactory(DjangoModelFactory):
    """A factory class used for creating Ingredients, only for testing purposes.
    """

    title = LazyAttribute(lambda obj: fake.text.title())
    quantity = LazyAttribute(lambda _: randint(20, 120))  # nosec


    class Meta:
        model = Ingredient
