from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from core.auth.serializers.register import UserRegisterSerializer, TeacherRegisterSerializer

class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken().for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({
            'user': serializer.data,
            'refresh': res['refresh'],
            'token': res['access'],
        }, status=status.HTTP_201_CREATED)

class TeacherRegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_classes = TeacherRegisterSerializer

    def post(self, request):
        serializer = self.serializer_classes(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        refresh = RefreshToken().for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return Response({
            'user': serializer.data,
            'refresh': res['refresh'],
            'token': res['access'],
        }, status=status.HTTP_201_CREATED)
