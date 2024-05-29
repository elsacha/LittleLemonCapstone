from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient
from restaurant import models
from restaurant import serializers
from restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = models.MenuItem.objects.create(title="Tiramisu", price=5.00, inventory=10)
        #self.menu_item2 = models.MenuItem.objects.create(title="Ceasar salad", price=10.00, inventory=5)

    # def test_getall(self):
    #     response = self.client.get('/restaurant/menu/items')
    #     menu_items = models.MenuItem.objects.all()
    #     serializer = serializers.MenuItemSerializer(menu_items, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, 200)
    
    def test_getall(self):
        request = RequestFactory().get('/restaurant/menu/items/')
        view = MenuItemsView()
        view.setup(request)

        context = str(view.get_queryset())
        self.assertIn('Tiramisu : 5.00', context)