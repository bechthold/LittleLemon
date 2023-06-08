from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Beef', price=150, inventory=10)
        Menu.objects.create(title='Fish', price=300, inventory=5)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()

        serializer = MenuSerializer(items, many=True)
        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
