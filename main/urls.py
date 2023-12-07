from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('home/<str:param>', views.home, name='home'),
    path('favorites/', views.favorites, name='favorites'),
    path('notifications/', views.notifications, name='notifications'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    # path('', views.test, name='test'),
    path('', views.landing, name='landing'),
    path('search=<str:search>', views.search_body, name="search_body"),
    path('add_post/<str:param>', views.add_post, name="add_post"),
    path('update_post/<int:id>', views.update_post, name="update_post"),
    path('delete_post/<int:id>', views.delete_post, name="delete_post"),
    path('visibility_post/<int:id>', views.visibility_post, name="visibility_post"),
    path('update_like/<int:post_id>/', views.update_like, name='update_like'),
    path('update_dislike/<int:post_id>/', views.update_dislike, name='update_dislike'),
    path('like_interaction/<int:user_id>/<int:post_id>/', views.like_interaction, name='like_interaction'),
    path('dislike_interaction/<int:user_id>/<int:post_id>/', views.dislike_interaction, name='dislike_interaction'),
    path('heart_interaction/<int:user_id>/<int:post_id>/', views.heart_interaction, name='heart_interaction'),
    path('add_comment/<int:user_id>/<int:post_id>/', views.add_comment, name='add_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('add_reply/<int:user_id>/<int:comment_id>/', views.add_reply, name="add_reply"),
]