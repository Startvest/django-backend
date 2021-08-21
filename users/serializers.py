from rest_framework import serializers
from .models import User, user_type
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(RegisterSerializer):
    username = None

    def save(self, request):
        user = super().save(request)
        user.save()
        return user

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_type
        fields = '__all__'
