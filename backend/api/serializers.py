from django.contrib.auth.models import User
from .models import CharInventory
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ("username", "password")
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            password=validated_data["password"]
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

class CharInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CharInventory
        fields = '__all__'

