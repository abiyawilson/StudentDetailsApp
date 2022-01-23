from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.models import CustomUser
from users.serializers import UserAccountSerializer


class UserAccountView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAccountSerializer


class UsersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserAccountSerializer


