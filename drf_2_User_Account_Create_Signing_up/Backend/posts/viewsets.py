from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404



class PostViewset(viewsets.ViewSet):
    def list(self, request:Request):
        queryset = Post.objects.all()
        
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request:Request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request:Request):
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Created",
                "data":serializer.data
            }        
                
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            response = {"message":"error':'Method PUT not allowed" }
                       
            return Response(data=response, status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(pk=pk)
        except:
            response = { "message":"error':'Post does not exists" }
               
           
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
        data = request.data
        
        serializer = PostSerializer(instance=post, data=data)        
        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Updated successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            response = {"message":"error':'Method DELETE not allowed"}
            return Response(data=response, status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(pk=pk)
        except:
            response = {"message":"error':'Post does not exists"}
            return Response(data=response)
        
        post.delete()
        response = {"message":" post " + str(pk) +  " deleted "}  
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)


class PostModelViewset(viewsets.ModelViewSet):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk' 
        
    
  

    