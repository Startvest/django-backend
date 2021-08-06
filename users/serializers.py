from rest_framework import serializers
from .models import User, user_type

class UserSerializer(serializers.ModelSerializer):
    username = None