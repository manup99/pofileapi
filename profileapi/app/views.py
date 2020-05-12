from rest_framework.views import APIView
from rest_framework.response import Response

class hello_world(APIView):
    def get(self,request,format=None):
        api_view=[
            'Just checking our api',
            'You can also check yourself',
        ]
        return Response({'Message':'Hello','api_view':api_view})