from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Ingredient,Drink

""" 
Run tests with python manage.py test bartender_app (specific test)

All files beginning with test will be included in the test run
"""

class DrinkViewsTests(APITestCase):
    """A class used for testing degree views.
    """

    def test_drinks_api(self):
        url = reverse('drink-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

