from rest_framework import serializers
from .models import User



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'email', 'first_name', 'last_name','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        raw_password = validated_data['password']
        user.set_password(raw_password)
        user.save()
        
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'    
