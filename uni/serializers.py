from rest_framework import serializers
from .models import University, User

class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'