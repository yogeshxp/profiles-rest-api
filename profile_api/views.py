from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View"""
    def get(self, request, formet=None):
        """Returns list of API features"""
        an_apiview = [
            'users HTTP Methods as function (get, post, patch, put, Delete)',
            'Is similer to Traditional Django view',
            'Gives You most application logic',
            'Is Mapped manually to URLs'
        ]

        return Response({'message':'hello', 'an_apiview':an_apiview})