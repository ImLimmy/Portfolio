from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'