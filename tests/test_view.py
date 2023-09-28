from django.test import TestCase
from Restaurant.models import *


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="test1", price=1, inventory=2)
        MenuItem.objects.create(title="test2", price=4, inventory=3)

    def test_getall(self):
        items = MenuItem.objects.all()
        self.assertIsInstance(items, dict)
