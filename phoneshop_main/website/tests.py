from django.test import TestCase
from .models import Category, Customer, Product, Order

# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Android')

    def test_string_representation(self):
        category = Category.objects.get(name='Android')
        self.assertEqual(str(category), 'Android')

class CustomModelTest(TestCase):
    def setUp(self):
        Customer.objects.create(
            first_name = 'Jennifer',
            last_name = 'Ann',
            phone = '0808676768',
            email = 'jennifer@admin.com',
            password = 'somepass'
        )
    
    def test_string_representation(self):
        customer = Customer.objects.get(email='jennifer@admin.com')
        self.assertEqual(str(customer), 'Jennifer Ann')

class ProductModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Electronics')
        Product.objects.create(
            name = 'Macbook',
            price = 1999,
            category = category,
            description = 'Apple Laptop',
            is_sale = True,
            sale_price = 1699,
        )
        Product.objects.create(
            name = 'Airpods',
            price = 129.99,
            category = category,
            description = 'Apple Airpods',
            is_sale = False,
            sale_price = 109.99,
        )
    
    def test_string_representation(self):
        product = Product.objects.get(name='Macbook')
        self.assertEqual(str(product), 'Macbook')
    
    def test_sale_price_true(self):
        product = Product.objects.get(name='Macbook')
        self.assertTrue(product.is_sale)
    
    def test_sale_price_false(self):
        product = Product.objects.get(name='Airpods')
        self.assertFalse(product.is_sale)
    
