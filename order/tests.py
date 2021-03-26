from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
import json

class OrdersTestcaseStaffUser(TestCase):
    """ 
        Test orders authenticated as staff ( Common User )
    """
               
    def setUp(self):
        self.order_sample = {"id":"1","status":"WAITING","consume_location": "INSHOP" ,"customer":"savio"}
        items = list()
        items.append({"id":"1","item":"Latte Milk whole","units": "3" })
        self.order_sample["items"] = items
        
        self.order_update_sample = {"id":"1","status":"CANCELED","consume_location": "INSHOP" ,"customer":"savio"}
        self.order_update_sample["items"] = items
        
        self.order_list = reverse('order-list') #GET, #POST
        self.order_detail = reverse('order-detail',args=[1]) # PUT, POST AND DELETE
        self.client = Client()
        self.staffuser = get_user_model().objects.create_user("admintest",
                                                              "admintest@admintest.com","admintest")
        self.client.login(username='admintest', password='admintest')
        
    def test_orders(self):       
        response = self.client.post(self.order_list,self.order_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 201)

        response = self.client.get(self.order_list,content_type='application/json') 
        self.assertEqual(response.status_code, 200)

        response = self.client.put(self.order_detail,self.order_update_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 403)
       
        response = self.client.put(self.order_detail,self.order_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 403)
       
        response = self.client.delete(self.order_detail) 
        self.assertEqual(response.status_code, 403)

class OrdersTestcaseSuperUser(TestCase):
    """ 
        Test orders authenticated as superuser
    """
               
    def setUp(self):
        self.order_sample = {"id":"1","status":"WAITING","consume_location": "INSHOP" ,"customer":"savio"}
        items = list()
        items.append({"id":"1","item":"Latte Milk whole","units": "3" })
        self.order_sample["items"] = items
        
        self.order_update_sample = {"id":"1","status":"CANCELED","consume_location": "INSHOP" ,"customer":"savio"}
        self.order_update_sample["items"] = items

        self.order_list = reverse('order-list') #GET, #POST
        self.order_detail = reverse('order-detail',args=[1]) # PUT, POST AND DELETE

        self.client = Client()
        self.staffuser = get_user_model().objects.create_superuser("admintest",
                                                              "admintest@admintest.com","admintest")
        self.client.login(username='admintest', password='admintest')
        
    def test_orders(self):
        response = self.client.post(self.order_list,self.order_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 201)

        response = self.client.get(self.order_list,content_type='application/json') 
        self.assertEqual(response.status_code, 200)

        response = self.client.put(self.order_detail,self.order_update_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 202)

        response = self.client.put(self.order_detail,self.order_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 403)

        response = self.client.delete(self.order_detail) # Exclude with status different of Waiting
        self.assertEqual(response.status_code, 403)

        response = self.client.post(self.order_list,self.order_sample,content_type='application/json') #New insertion status=Waiting
        self.assertEqual(response.status_code, 201)

        response = self.client.delete(reverse('order-detail',args=[2])) # Exclude with status equal to Waiting
        self.assertEqual(response.status_code, 202)
        
        

class OrdersTestcaseNoAuthenticated(TestCase):
    """ 
        Test orders with no user authentication
    """
               
    def setUp(self):
        self.order_sample = {"id":"1","status":"WAITING","consume_location": "INSHOP" ,"customer":"savio"}
        items = list()
        items.append({"id":"1","item":"Latte Milk whole","units": "3" })
        self.order_sample["items"] = items
        
        self.order_update_sample = {"id":"1","status":"CANCELED","consume_location": "INSHOP" ,"customer":"savio"}
        self.order_update_sample["items"] = items

        self.order_list = reverse('order-list') #GET, #POST
        self.order_detail = reverse('order-detail',args=[1]) # PUT, POST AND DELETE

        self.client = Client()
        self.staffuser = get_user_model().objects.create_superuser("admintest",
                                                              "admintest@admintest.com","admintest")
        
    def test_orders(self):
        response = self.client.post(self.order_list,self.order_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 401)

        response = self.client.get(self.order_list,content_type='application/json') 
        self.assertEqual(response.status_code, 401)

        response = self.client.put(self.order_detail,self.order_update_sample,content_type='application/json') 
        self.assertEqual(response.status_code, 401)

        response = self.client.delete(self.order_detail) 
        self.assertEqual(response.status_code, 401)