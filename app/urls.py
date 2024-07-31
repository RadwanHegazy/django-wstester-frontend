from .views import home
from .views.auth import login, register, logout
from django.urls import path

urlpatterns = [
    path('user/auth/login/', login.LoginView.as_view(),name='login'),    
    path('user/auth/logout/', logout.LogoutView.as_view(),name='logout'),    
    path('user/auth/register/', register.RegisterView.as_view(),name='register'),

    path('', home.HomeView.as_view(),name='home')    
]