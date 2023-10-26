from django.shortcuts import render
from .serializers import SingUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request



class SingUpView(generics.GenericAPIView):
    serializer_class = SingUpSerializer

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"User created successfully",
                "data":serializer.data
                
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)