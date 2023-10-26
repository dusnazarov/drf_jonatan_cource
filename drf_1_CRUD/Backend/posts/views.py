from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



# # ///////////// Home ///////////////////
def home(request: HttpRequest):
    response = {"message": "Hello world"}
    return JsonResponse(data=response)


@api_view(http_method_names=["GET", "POST"])
def home_list_create(request: Request):

    if request.method == "POST":
        data = request.data
        
        response = {
            "message": "Hello world",
            "data":data
        }

        return Response(data=response, status=status.HTTP_201_CREATED)
        
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)


# # ////// CRUD  Function Based View (1) ////////
@api_view(http_method_names=["GET", "POST"])
def home_list_create_view(request: Request):

    if request.method == "POST":
        data = request.data
        
        response = {
            "message": "Hello world",
            "data":data
        }        
        return Response(data=response, status=status.HTTP_201_CREATED)
        
    response = {"message": "Hello world"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST"])
def post_list_create_view(request: Request):
    posts = Post.objects.all()

    if request.method == "POST":
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post Created",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)

    response = {
        "message": "posts",
        "data": serializer.data
    }      
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail_view(request: Request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post)

    response = {
        "message":"post",
        "data":serializer.data
    }    
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["PUT"])
def post_update_view(request: Request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    data = request.data
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message":"Post Updated Successfully",
            "data":serializer.data
        }

        return Response(data=response, status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(http_method_names=["DELETE"])
def post_delete_view(request: Request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# # ////// CRUD  Function Based View (2)  ////////
@api_view(['GET','POST','PUT', 'DELETE'])
def post_list_create_update_delete_view(request, post_id=None, *args, **kwargs):
        
    if request.method == "GET": 
        if post_id is not None:
            post = get_object_or_404(Post, pk=post_id)
            serializer = PostSerializer(instance=post, many=False)
            response = {
               "message":"Post Detail",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
             
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        response = {
            "message":"List of Posts",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        data = request.data           
        serializer = PostSerializer(data=data)        
        if serializer.is_valid():           
            serializer.save()
            response = {
                "message":"Post Created",
                "data":serializer.data
            }            
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {"message":"invalid : Not Good Data"}        
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        post = get_object_or_404(Post, pk=post_id)
        data = request.data         
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"Post Updated successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        response = {"message":"invalid: Not Good Data" }
        return Response({"invalid":"not good data"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

  
# # ////// CRUD Class Based View (APIView (1)) ////////

class PostListCreateAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request: Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
       
        

    def post(self, request: Request, *args, **kwargs):
        data = self.request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Created",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = PostSerializer
    
    def get(self, request:Request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request:Request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        data = request.data

        serializer = self.serializer_class(instance=post, data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Updated",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request:Request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# # ///////// CRUD Class Based View (APIView (2)) //////////////////////////////////////
class PostListCreateUpdateDeleteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('post_id', None)

        if not pk:
            posts = Post.objects.all()
            serializer = PostSerializer(instance=posts, many=True)

            response = {
                "message":"List Posts",
                "data":serializer.data
                
            }
            return Response(data=response, status=status.HTTP_200_OK )
        if pk:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(instance=post, many=False)

            response = {
                "message":"Post Detail",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)    
    
    def post(self, request):
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
    
    def put(self, request, *args, **kwargs):
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
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            response = {"message":"error - Method DELETE not allowed"}
            return Response(data=response, status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(pk=pk)
        except:
            response = {"message":"error - Post does not exists"}
            return Response(data=response)
        
        post.delete()
        response = {"message":" post " + str(pk) +  " deleted "}  
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)


# # ////// CRUD Class Based View (generics and mixins) ////////

class PostListCreateGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
   

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request: Request, *args, **kwargs):
       return self.create(request, *args, **kwargs)    
       

class PostRetrieveUpdateDeleteGenericAPIView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
        
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# # ////////////////////  generics   ////////////////////////////
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# # ///////////////// CRUD Class Based View ( ModelViewset)  //////////////////////////////////
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

       

    

   



   

      
 
    
    

