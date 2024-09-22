#from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes  # Import permission_classes
from rest_framework.permissions import AllowAny  # Import AllowAny permission
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])  # Allow anyone to access this view without authentication
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)
    request.user.following.add(user_to_follow)
    return Response({'message': f'You are now following {user_to_follow.username}'}, status=200)

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = User.objects.get(id=user_id)
    request.user.following.remove(user_to_unfollow)
    return Response({'message': f'You have unfollowed {user_to_unfollow.username}'}, status=200)


from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')  # Ensure the path is correct

def register_view(request):
    return render(request, 'accounts/register.html')

