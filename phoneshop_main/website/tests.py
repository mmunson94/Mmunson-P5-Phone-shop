from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, Customer, Product, Order
from django.contrib.auth.models import User


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
    
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='jhvugu!',)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_newsletters_view(self):
        response = self.client.get(reverse('newsletters'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletters.html')

    def test_add_product_view_not_available_for_non_admin(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 302)
    
    def test_404(self):
        response = self.client.get('/random-url-that-doesnt-exist')
        self.assertEqual(response.status_code, 404) 
        self.assertTemplateUsed(response, '404.html')

class AdminViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(
            username='John', password='123456789!', email='test@gmail.com')
        self.client.login(username='John', password='123456789!')

    def test_add_product_view_opens_for_admin(self):
        response = self.client.get(reverse('add_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_product.html')