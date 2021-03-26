from rest_framework.viewsets import ModelViewSet
from customer.models import Userauth
from .serializers import UserauthSerializer
from rest_framework.permissions import AllowAny

class UserauthViewSet(ModelViewSet):
	"""
		** Authentication NOT required for this actions **
  
		GET: List all users, regardless the type of user that request **(SUEPERUSER OR STAFF USER)**
		
		POST: Create a new user, all type of users are allowed to create, all fiels are mandatory
		
		{
			"username":"STRING",
			"password":"STRING",
			"email":"STRING",
			"password_confirm":"STRING",
			"is_staff":BOOL,
			"is_superuser":BOOL
		}

	"""
	permission_classes = [AllowAny]
	queryset = Userauth.objects.all()
	serializer_class = UserauthSerializer