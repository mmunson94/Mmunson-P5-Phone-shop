from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='jhvugu!',)

    def test_open_cart_summary_view(self):
        response = self.client.get(reverse('cart_summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart_summary.html')