from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view  # Ensure this is imported
from rest_framework.response import Response  # Ensure this is imported
from .models import Post, Like  # Import your models
from django.contrib.contenttypes.models import ContentType  # Needed for content type usage
from notifications.models import Notification  # Import Notification model


# Create your views here

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(['GET'])
def user_feed(request):
    followed_users = request.user.following.all()
    posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)  # Find the post by ID
    Like.objects.get_or_create(user=request.user, post=post)  # Create the Like object
    
    # Create a notification for the post author if the liker is not the author
    post_author = post.author
    if request.user != post_author:  # Avoid self-notifications
        Notification.objects.create(
            recipient=post_author,
            actor=request.user,
            verb='liked',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )
    
    return Response({'message': 'Post liked'}, status=200)
