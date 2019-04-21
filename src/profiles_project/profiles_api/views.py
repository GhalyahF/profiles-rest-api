from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers


class HelloApiView(APIView):
    serializer_class= serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview= [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'an_apiview': an_apiview})


    def post(self, request):
        serializer= serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message= "Hello {0}".format(name)
            return Response({'message': message})
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response ({'method':'put'})


    def patch(self, request, pk=None):
        return Response ({'method':'patch'})


    def delete(self, request, pk=None):
        return Response ({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    def list(self,request):
            a_viewset = [
                'Uses actions (list,create, retrieve,update,partially update,)',
                'Automatically maps to urls using Routers',
                'Provides more functionality with less code',

            ]
            return Response ({'a_viewset':a_viewset})
