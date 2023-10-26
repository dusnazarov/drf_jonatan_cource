from django.urls import path
from .import views

urlpatterns = [
    
    path('home/', views.home, name='home_page'),  
    path('home/list/', views.home_list_create, name='home_list'),
    path('home/create/', views.home_list_create, name='home_create' ),

    # ////// CRUD  Function Based View (1) ////////
    path('list/', views.post_list_create_view, name='post_list' ),
    path('create/', views.post_list_create_view, name='post_create' ),
    path('detail/<int:post_id>/', views.post_detail_view, name='post_detail' ),
    path('update/<int:post_id>/', views.post_update_view, name='post_update'),
    path('delete/<int:post_id>/', views.post_delete_view, name='post_delete'),

    # ////// CRUD  Function Based View (2) ////////
    path('2list/', views.post_list_create_update_delete_view, name='post2_list' ),
    path('2create/', views.post_list_create_update_delete_view, name='post2_create' ),
    path('2detail/<int:post_id>/', views.post_list_create_update_delete_view, name='post2_detail' ),
    path('2update/<int:post_id>/', views.post_list_create_update_delete_view, name='post2_update'),
    path('2delete/<int:post_id>/', views.post_list_create_update_delete_view, name='post2_delete'),

    
    # ////// CRUD Class Based View (APIView (1)) ////////
    path('c_list/', views.PostListCreateAPIView.as_view(), name='c_post_list' ),
    path('c_create/', views.PostListCreateAPIView.as_view(), name='c_post_create' ),
    path('c_detail/<int:post_id>/', views.PostRetrieveUpdateDeleteAPIView.as_view(), name='c_post_detail' ),
    path('c_update/<int:post_id>/', views.PostRetrieveUpdateDeleteAPIView.as_view(), name='c_post_update'),
    path('c_delete/<int:post_id>/', views.PostRetrieveUpdateDeleteAPIView.as_view(), name='c_post_delete'),

    # ////// CRUD Class Based View (APIView (2)) ////////
    path('2c_list/', views.PostListCreateUpdateDeleteAPIView.as_view(), name='2c_post_list' ),
    path('2c_create/', views.PostListCreateUpdateDeleteAPIView.as_view(), name='2c_post_create' ),
    path('2c_detail/<int:post_id>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name='2c_post_detail' ),
    path('2c_update/<int:post_id>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name='2c_post_update'),
    path('2c_delete/<int:post_id>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name='2c_post_delete'),



    # ////// CRUD Class Based View (generics and mixins) ////////
    path('g_list/', views.PostListCreateGenericAPIView.as_view(), name='g_post_list' ),
    path('g_create/', views.PostListCreateGenericAPIView.as_view(), name='g_post_create'),
    path('g_detail/<int:pk>/', views.PostRetrieveUpdateDeleteGenericAPIView.as_view(), name='g_post_detail' ),
    path('g_update/<int:pk>/', views.PostRetrieveUpdateDeleteGenericAPIView.as_view(), name='g_post_update'),
    path('g_delete/<int:pk>/', views.PostRetrieveUpdateDeleteGenericAPIView.as_view(), name='g_post_delete'), 


    # ////// CRUD Class Based View ( generics ) ////////
    path('ge_list/', views.PostListCreateAPIView.as_view(), name='ge_post_list' ),
    path('ge_create/', views.PostListCreateAPIView.as_view(), name='ge_post_create'),
    path('ge_detail/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='ge_post_detail' ),
    path('ge_update/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='ge_post_update'),
    path('ge_delete/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='ge_post_delete'), 


    # # ////////////////////  ModelViewset   //////////////////////////// 

    path('vlist/', views.PostViewSet.as_view({'get':'list'})),
    path('vdetail/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve'})),
    path('vcreate/', views.PostViewSet.as_view({'post':'create'})),   
    path('vupdate/<int:pk>', views.PostViewSet.as_view({'put':'update'})),
    path('vdelete/<int:pk>', views.PostViewSet.as_view({'delete':'destroy'})),          
    
]







