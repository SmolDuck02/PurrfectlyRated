from django.urls import path

from . import views


app_name = 'authentication'

urlpatterns = [
    path('', views.myfirst, name='myfirst'),
    path('admin/', views.admin, name='admin'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('delete_account/<int:id>', views.delete_account, name='delete_account'),
]