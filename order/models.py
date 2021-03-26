from .orderstatus import OrderStatus
from .consumelocation import ConsumeLocation
from django.db import models
from product.models import Product
from customer.models import Userauth

class Order(models.Model):
    ''' 
        Entity that registry customer order adding the items
    '''
    id = models.AutoField(primary_key=True)
    customer = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=OrderStatus.Selected()) 
    consume_location = models.CharField(max_length=255, choices=ConsumeLocation.Selected())

    def __str__(self):
        return self.customer +' '+str(self.id)+' '+ self.status

class Items(models.Model):
    ''' 
        Entity item unit
    '''
    id = models.AutoField(primary_key=True)
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    item = models.CharField(max_length=255)
    units = models.IntegerField(default=1)