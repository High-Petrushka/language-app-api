from rest_framework import serializers

from core.user.serializers import UserSerializer
from core.teacher.serializers import TeacherSerializer

from core.user.models import MyUser
from core.teacher.models import Teacher

class UserRegisterSerializer(UserSerializer):
    pass

class TeacherRegisterSerializer(TeacherSerializer):
    pass