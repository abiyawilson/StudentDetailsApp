from rest_framework import serializers

from studentDetailsApi.models import StudentTShirtDetails


class StudentTShirtDetailsSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user')

    class Meta:
        model = StudentTShirtDetails
        fields = '__all__'
