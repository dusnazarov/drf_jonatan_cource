from django.http import HttpRequest, JsonResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes

from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, mixins, status
    

from rest_framework.permissions import  AllowAny, IsAuthenticatedOrReadOnly 
from .permissions import ReadOnly
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema




# # //////////////////// ////////////////////////////

class CustomPaginator(PageNumberPagination):
    page_size = 2
    page_query_param = "page"
    page_size_query_param = "page_size"

@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
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

class PostListCreateAPIView(
        generics.ListCreateAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin
    ):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 
    pagination_class = CustomPaginator  
    queryset = Post.objects.all()


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
      
    
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnly]    
    serializer_class = PostSerializer    
    queryset = Post.objects.all()


class ListPostsForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator

    # def get_queryset(self):
    #     user = self.request.user

    #     return Post.objects.filter(author=user)


    # http://127.0.0.1:8000/posts/post_for/admin
    # def get_queryset(self):        
    #     username = self.kwargs.get("username")

    #     return Post.objects.filter(author__username=username)
    
    # http://127.0.0.1:8000/posts/post_for/?username=admin
    def get_queryset(self):        
        username = self.request.query_params.get("username") or None

        queryset = Post.objects.all()

        if username is not None:
            return Post.objects.filter(author__username=username)
        return  queryset      

        
    @swagger_auto_schema(
        operation_summary="List all posts",
        operation_description="This returns a list of all posts"
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)






       

    

   



   

      
 
    
    

