from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()# customUser
        fields = ('username','bio', 'profile_picture','followers')

# This serializer handles user registration ensures password is write only wont be returned in the response
class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username','email','password')

    def create(self,validated_data):
            user = get_user_model().objects.create_user( # the create_user handles the password hashing
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password'],

            )
            Token.objects.create(user=user) # creating a token for the user after registration
            return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
