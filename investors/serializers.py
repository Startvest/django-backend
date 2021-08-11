from rest_framework import serializers
from .models import Investor, Investment


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
    
class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['registered_business', 'interests', 'verified']
    
    investments = InvestmentSerializer(many=True, read_only=True)