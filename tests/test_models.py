from django.test import TestCase
from Restaurant.models import *


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Yogurt", price=60, inventory=120)
        self.assertEqual(item, "Yogurt:80")
