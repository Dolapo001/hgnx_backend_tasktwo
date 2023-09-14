from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)

    class Meta:
        model = Person
        fields = ('id', 'name', 'age', 'email')


    @staticmethod
    def validate_name(value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        return value

