from django.test import TestCase
from .models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Test Product", price=10.99)

    def test_product_price(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.price, 10.99)
