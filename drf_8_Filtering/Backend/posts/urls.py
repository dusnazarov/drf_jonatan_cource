from django.urls import path
from .import views

urlpatterns = [
    
    path('home/', views.home_list_create, name='home'),
    path('list/', views.PostListCreateAPIView.as_view(), name='post_list' ),
    path('create/', views.PostListCreateAPIView.as_view(), name='post_create'),
    path('detail/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail' ),
    path('update/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_delete'),

     
    path('post_for_current_user/', views.ListPostsForAuthor.as_view(), name='post_current_user'),
    
    # http://127.0.0.1:8000/posts/post_for/admin 
    path('post_for/<username>', views.ListPostsForAuthor.as_view(), name='post_current_user'),
        
    # http://127.0.0.1:8000/posts/post_for/?username=admin
    path('post_for/', views.ListPostsForAuthor.as_view(), name='post_current_user'), 

       
    
]







