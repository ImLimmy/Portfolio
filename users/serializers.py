from rest_framework import serializers

from .models import CustomUser

class User(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    
class UserDetail(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'image', 'fullname', 'Bio', 'Tagline', 'address', 'email', 'contact_number')
        

class UserUpdate(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'