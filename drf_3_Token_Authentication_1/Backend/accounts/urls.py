from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SingUpView.as_view(), name='singup'),
    path('login/', views.LoginView.as_view(), name='login')
]
