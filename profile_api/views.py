from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers


class HelloApiView(APIView):
    """ Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API features"""
        an_apiview = [
            'users HTTP Methods as function (get, post, patch, put, Delete)',
            'Is similar to Traditional Django view',
            'Gives You most application logic',
            'Is Mapped manually to URLs'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an Object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle a partial update of an Object"""
        return Response({'method': 'DELETE'})
