from rest_framework import serializers

from core.user.serializers import UserSerializer
from core.teacher.serializers import TeacherSerializer

from core.user.models import MyUser
from core.teacher.models import Teacher

class UserRegisterSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'avatar', 'password']

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)

class TeacherRegisterSerializer(TeacherSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True
    )

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'bio', 'password']

