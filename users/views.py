from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, user_type
from .serializers import UserTypeSerializer

from startups.views import MultipleFieldLookupMixin
from permissions import IsOwner

# Create your views here.
@api_view(['POST', ])
def create_user_type(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
   

    data = request.data.copy()
    data['user'] = user.id

    serializer = UserTypeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserTypeInfo(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    permission_classes = [IsOwner]
    queryset = user_type.objects.all()
    serializer_class = UserTypeSerializer
    lookup_fields = ['user_id']