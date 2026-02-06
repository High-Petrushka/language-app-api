from rest_framework import serializers
from core.user.models import MyUser

class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'avatar', 'is_active', 'created_at', 'updated_at']
        read_only_field = ['is_active']
