from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

class ProductsTestcase(TestCase):
               
    def setUp(self):
    
        self.get_product = reverse('product_list')
        self.client = Client()
        self.user = get_user_model().objects.create_superuser("admintest",
                                                              "admintest@admintest.com","admintest")
        self.client.login(username='admintest', password='admintest')
        
    def test_list_products_authenticated(self):
        """ 
            Test to List all products
        """
        response = self.client.get(self.get_product,format='json') 
        self.assertEqual(response.status_code, 200)
    
    def test_list_products_no_authenticated(self):
        """ 
            Test to List all products
        """
        self.client.logout()
        response = self.client.get(self.get_product,format='json') 
        self.assertEqual(response.status_code, 401)