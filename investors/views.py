from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Investor, Investment
from .serializers import InvestorSerializer

from startups.models import Startup

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


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


class InvestorsList(generics.ListAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestorsInfo(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
    lookup_fields = ['user_id']


@api_view(['POST', ])
def create_investor(request, uid):
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
   
    user = user_type(is_investor=True, user=user)
    serializer = InvestorSerializer(user, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
def update_investor_info(request, uid):
    try:
        investor = Investor.objects.get(pk=uid)
    except Investor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = InvestorSerializer(startup, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data[SUCCESS] = UPDATE_SUCCESS
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', ])
def invest(request):
    try:
        investor = Investor.objects.get(pk=request.data.get('investor'))
        startup = Startup.objects.get(pk=request.data.get('startup'))
    except Investor.DoesNotExist or Startup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    investment = Investment(investor=investor, startup=startup)
    serializer = InvestmentSerializer(investment, data=request.data)
    data = {}
    if serializer.is_valid():
        startup.deposit(request.data.get('amount'))
        serializer.save()
        data[SUCCESS] = CREATE_SUCCESS
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)