from rest_framework import serializers
from .models import User, user_type
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(RegisterSerializer):
    # class Meta:
    #     model = User
    #     fields = ['email', 'password']
    #     extra_kwargs = {'password': {'write_only': True}}
    

    # def create(self, validated_data):
    #     user = User(email=validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user

    username = None

    def save(self, request):
        user = super().save(request)
        user.save()
        return user