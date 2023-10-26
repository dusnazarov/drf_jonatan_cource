from django.shortcuts import render
from .serializers import SingUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema  


class SingUpView(generics.GenericAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = SingUpSerializer

    @swagger_auto_schema(
        operation_summary="Create a user account",
        operation_description="This sign up a user"
    )
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


class LoginView(APIView):
    permission_classes =[ IsAuthenticated]
    
    @swagger_auto_schema(
        operation_summary="Generate JWT pair",
        operation_description="This login a user"
    )
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')        
        

        user = authenticate(email=email, password=password)
        print(user)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message":"Login Successfully",
                "tokens":tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})
        
    @swagger_auto_schema(
        operation_summary="Get request info",
        operation_description="This shows the request info"
    )
    def get(self, request:Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }
        
        return Response(data=content, status=status.HTTP_200_OK)
        