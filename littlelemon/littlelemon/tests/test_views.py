from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(ID=3, Title="Pizza", Price=80, Inventory=100)
        Menu.objects.create(ID=4, Title="Burger", Price=50, Inventory=50)
    def test_getall(self):
        item1 = Menu.objects.get(ID=3)
        item2 = Menu.objects.get(ID=4)
        self.assertEqual(str(item1), "Pizza : 80.00")
        self.assertEqual(str(item2), "Burger : 50.00")

        
