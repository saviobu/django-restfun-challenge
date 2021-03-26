from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from order.models import Order,Items
from .serializers import OrderSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

class OrderViewSet(ModelViewSet):
	"""
		**Authentication is Mandatory for this actions**
  
		GET:
			Return the list of orders, if the user is **basic** user 
			the return wille be only his orders, but if the user is **superuser**
			the return will be all orders in database.
			**( DON'T HAVE BODY )**

		POST:
			Will create a new order since filled all required fields:
			**STATUS FIELD OPTIONS ( WAITING,READY,CANCELEDc)**
			**CONSUME_LOCATION FIELD OPTIONS ( INSHOP,TAKEAWAY )**
			
			{
				"status":"string", 						
				"consume_location": "string",   
				"customer":"string", 					
				"items": [
					{
						"item":"string",		**Required field
						"units":int				**Required field
					}
				]
			}

		DELETE: 
			Delete an specific order by order id, only **superusers** can do  it. **( DON'T HAVE BODY )
			**( ONLY SUPERUSER CAN EXECUTE THIS ACTION )**

		PUT:
			Update an especific order by order id **( MUST BE PASSED ON THE URL)**, only **superusers**, 
			the changes must be passed in the body, **all fields** are mandatory, and just orders with 
			status "WAITIG" can be updated ( THE BODY IS SAME OF POST )
   			**( ONLY SUPERUSER CAN EXECUTE THIS ACTION )**

      		
	"""
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	
	"""
		Getting username to bring only his/her orders, if doesn't superuser
		on this case bring all orders
 	"""
	def get_queryset(self):
		request_username = self.request.user.username
		query = self.queryset
		if not self.request.user.is_superuser:
			return query.filter(customer=request_username)
		return query.all()
	
	"""
		Update an Order, including Items, if the order status is WAITING, only superuser can
		change order status
	"""

	def update(self, request,pk=None):
		if self.request.user.is_superuser:
			order_to_update = Order.objects.filter(id=pk).first()
			if order_to_update:
				if order_to_update.status == "WAITING":
					order_updated_serialized_data = request
					with transaction.atomic():
						order_updated_data = order_updated_serialized_data.data
						items_data = request.data.pop('items')

						try:
							Order.objects.filter(id=pk).update(**order_updated_data)

							for item in items_data:
								Items.objects.filter(id=item['id']).update(**item)
							
							update_result=request.data
							update_result['items']=items_data
							return Response(data=update_result, status=202)
						except Exception as exc:
							return Response(status=500,data=str(exc))
					return Response(status=500)
				return Response(status=403)
			return Response(status=404)
		return Response(status=403)

	"""
		Exclude an Order, including Items, if the order status is WAITING, only superusers
		are allowed to do it
	"""

	def destroy(self, request, pk=None):
		if self.request.user.is_superuser:
			order_to_exclude = Order.objects.filter(id=pk).first()
			if order_to_exclude:
				if order_to_exclude.status == "WAITING":
					with transaction.atomic():
						Order.objects.filter(id=pk).delete()
					return Response(status=202)
				return Response(status=403)
			return Response(status=404)
		return Response(status=403)