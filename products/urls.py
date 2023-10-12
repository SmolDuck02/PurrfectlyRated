
from django.urls import path
from . import views

app_name = 'products'


urlpatterns = [
    path('', views.jameel, name='jameel'),
    path('routes/', views.routes, name='routes'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('users/', views.users, name='users'),
    path('home/', views.home, name='home'),
    path('users/create/', views.createUser, name='create-user'),
    path('users/<str:pk>/update/', views.updateUser, name='update-user'),
    path('users/<str:pk>/delete/', views.deleteUser, name='delete-user'),
    
    path('users/<str:pk>/', views.user, name='user'),
    
    
]