from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status
from rest_framework import viewsets
class hello_world(APIView):
    serializer_class=HelloSerializer
    def get(self,request,format=None):
        api_view=[
            'Just checking our api',
            'You can also check yourself',
        ]
        return Response({'Message':'Hello','api_view':api_view})
    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_viewset=[
            'User actions (list,create,retireve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more fucntionaity with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})
    def update(self,request,pk=None):
        """Updating an object"""
        return Response({'http_method':'PATCH'})
    def partial_update(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'PATCH'})
    def destroy(self,request,pk=None):
        """Destroy an object"""
        return Response({'http_method':'DELETE'})

