
from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Post
from .serializers import PostSerializer
from rest_framework.generics import(  
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated  



# # ////////////////////  generics   ////////////////////////////
class PostListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer






       

    

   



   

      
 
    
    

