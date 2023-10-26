from django.urls import path
from .import views

urlpatterns = [

    path('list/', views.PostListCreateAPIView.as_view(), name='post_list' ),
    path('create/', views.PostListCreateAPIView.as_view(), name='post_create'),
    path('detail/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_detail' ),
    path('update/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post_delete'), 

       
    
]







