from django.urls import path
from .views import register, login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]


from .views import follow_user, unfollow_user
from posts.views import user_feed

urlpatterns += [
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
    path('feed/', user_feed, name='user_feed'),
]
