from rest_framework import serializers, fields
from order.models import Order,Items


class OrderItems(serializers.ModelSerializer):
	class Meta:
		model = Items	
		fields = ('id','item','units')
  
class OrderSerializer(serializers.ModelSerializer):
	items = OrderItems(many=True)
	class Meta:
		model = Order
		fields = ('id','customer','status','consume_location','items')
  
	"""
		Insert Order in database
	"""
	
	def create(self, request):
		items_data = request.pop('items')
		order = Order.objects.create(**request)
		for item in items_data:
			Items.objects.create(id_order=order, **item)
		return order