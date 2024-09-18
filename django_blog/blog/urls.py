from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, register, profile, add_comment, CommentUpdateView, CommentDeleteView
from django.contrib.auth import views as auth_views
from .views import PostByTagListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('posts/new/', PostCreateView.as_view(), name='post_create'),
    #path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    #path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Add this line
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
    ath('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
