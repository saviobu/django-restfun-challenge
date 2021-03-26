from rest_framework.response import Response
from product.models import InstantiateAll
from rest_framework.decorators import api_view
import json

"""
	** Authenticatios is required for this action **

	GET: **Always** return a list of all products (Menu), **don't** return an especific 
	product available all users are allowed. 
"""

@api_view(['GET'])
def get_product_list(self):	
	objects = InstantiateAll()
	jsonobject = json.loads(json.dumps([ob.__dict__ for ob in objects()]))
	return Response(jsonobject)