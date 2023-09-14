from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.Charfield(required=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email')

    @staticmethod
    def validate_name(value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        return value

