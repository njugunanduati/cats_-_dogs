from rest_framework import serializers
from django.contrib.auth.models import User
from pets.models import Pet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'pet_type', 'description', 'birth_date', 'date_added', 'owner']