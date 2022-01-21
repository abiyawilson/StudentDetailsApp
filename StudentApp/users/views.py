from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.models import CustomUser
from users.serializers import UserAccountSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class UserAccountView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAccountSerializer


class UsersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserAccountSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })
