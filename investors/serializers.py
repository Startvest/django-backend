from rest_framework import serializers
from .models import Investor, Investment


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'

    
class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = '__all__'
    
    investments = InvestmentSerializer(many=True, read_only=True)