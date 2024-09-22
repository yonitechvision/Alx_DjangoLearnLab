from django.urls import path
from .views import FeedViewSet

urlpatterns = [
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='feed'),
       path('<int:pk>/like/', PostViewSet.as_view({'post': 'like_post'}), name='like_post'),
    path('<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike_post'}), name='unlike_post'),
]
