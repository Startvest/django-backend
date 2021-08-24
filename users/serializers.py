from rest_framework import serializers
from .models import User, user_type
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = '__all__'

    username = None

class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_type
        fields = '__all__'

class GetUserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_type
        fields = '__all__'

    user = UserSerializer(many=False, read_only=True)


