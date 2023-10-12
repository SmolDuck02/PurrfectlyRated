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
    path('update_post/<int:id>', views.update_post, name="update_post"),
    path('delete_post/<int:id>', views.delete_post, name="delete_post"),
    path('undelete_post/<int:id>', views.undelete_post, name="undelete_post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)