from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('home/', views.home, name='home'),
    # path('', views.test, name='test'),
    path('', views.landing, name='landing'),
    path('search/<str:search>', views.search_body, name="search_body"),
    path('add_post/<str:param>', views.add_post, name="add_post"),
    path('update_post/<int:id>', views.update_post, name="update_post"),
    path('visibility_post/<int:id>', views.visibility_post, name="visibility_post"),
]
