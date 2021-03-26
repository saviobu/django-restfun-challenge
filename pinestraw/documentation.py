from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger.renderers import OpenAPIRenderer,SwaggerUIRenderer
from rest_framework.renderers import CoreJSONRenderer


class Schema(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        CoreJSONRenderer,
        OpenAPIRenderer,
        SwaggerUIRenderer
    ]

    def get(self,request):
        generator = SchemaGenerator(title='Pinestraw Project',version='1.0.0')
        schema = generator.get_schema()
        return Response(schema)