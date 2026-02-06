from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from core.user.models import MyUser
from core.user.serializers import UserSerializer

# A view allowing to see the list of all the students only for admin users
class UsersView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get(self):
        users = MyUser.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

# A view that allows particular user to see and edit his/her profile
class UserProfileView(APIView):
    serializer_class = UserSerializer

    def get_object(self, pk):
        try:
            return MyUser.objects.get(pk=pk)
        except MyUser.DoesNotExist:
            return Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
