from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Startup, JobOpening
from .serializers import StartupSerializer, JobOpeningSerializer
from users.models import User, user_type

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()             
        queryset = self.filter_queryset(queryset)  
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj


class StartupsList(generics.ListAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer

class StartupsInfo(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    lookup_fields = ['user_id']

@api_view(['POST', ])
def create_startup(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
   
    user = user_type(is_startup=True, user=user)
    serializer = StartupSerializer(user, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
def update_startup_info(request, uid):
    try:
        startup = Startup.objects.get(pk=uid)
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = StartupSerializer(startup, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data[SUCCESS] = UPDATE_SUCCESS
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', ])
def withdraw(request):
    try:
        startup = Startup.objects.get(pk=request.data.get('user'))
    except Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    withdrawal = startup.withdraw(request.data.get('amount'))

    if withdrawal:
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)