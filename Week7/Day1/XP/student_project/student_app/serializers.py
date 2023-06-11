from .models import Student
from rest_framework import serializers

# create serializer:
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # the fields we want to serialize:
        fields = ('first_name', 'last_name', 'email', 'date_joined')