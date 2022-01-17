from rest_framework import serializers

from studentDetailsApi.models import StudentTShirtDetails


class StudentTShirtDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentTShirtDetails
        # field = ['id', 'first_name', 'last_name', 'age', 'email_id', 'section', 'shirt_size', 'guardian_name',
        #          'guardian_phone_number', 'created']
        fields = '__all__'
