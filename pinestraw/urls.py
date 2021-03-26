from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from customer.api.viewsets import UserauthViewSet
from order.api.viewsets import OrderViewSet
from rest_framework.schemas import get_schema_view, SchemaGenerator
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework import permissions
from rest_framework.renderers import DocumentationRenderer
from product.api import viewsets

schema_view = get_schema_view(title='Pinestraw Project',permission_classes=(permissions.AllowAny,),
public=True,description='Pinestraw Test API Documentation',version='1.0.0')

DocumentationRenderer.languages = ['python']

router = routers.DefaultRouter()
router.register(r'customer', UserauthViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [

    path('v1/', include(router.urls)),
    path('v1/auth/login/', obtain_jwt_token), 
    path('v1/auth/refresh-token/', refresh_jwt_token), 
    path('v1/docs/', schema_view, name='Pinestraw API Documentation'),
    path('v1/product/', viewsets.get_product_list,name='product_list'),
]