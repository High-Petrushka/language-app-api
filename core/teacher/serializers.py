from rest_framework import serializers
from core.teacher.models import Teacher, BankInfo

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'bio', 'card_info', 'is_active']
        read_only_field = ['is_active']

class BankInfoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = BankInfo
        fields = ['card_number', 'expiration_date', 'cvv_code', 'created_at', 'updated_at']