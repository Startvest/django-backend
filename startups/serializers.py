from users.serializers import GetUserTypeSerializer, UserSerializer
from rest_framework import serializers
from .models import Startup, JobOpening, StartupGallery


class StartupGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupGallery
        fields = '__all__'

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'

class GetJobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

    company = StartupSerializer(many=False, read_only=True)

class GetStartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'

    jobs = JobOpeningSerializer(many=True, read_only=True)
    gallery = StartupGallerySerializer(many=True, read_only=True)
    user = GetUserTypeSerializer(many=False, read_only=True)