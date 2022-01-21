from rest_framework import serializers

from users.models import CustomUser


class UserAccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2', 'is_staff', 'is_active', 'studentsDetails')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        account = CustomUser(
            email=self.validated_data['email'],
            is_staff=self.validated_data['is_staff'],
            is_active=self.validated_data['is_active']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Password must match'})
        account.set_password(password)
        account.save()
