from rest_framework import serializers
from django.contrib.auth.models import User

# import default Django password hashing function
from django.contrib.auth.hashers import make_password
from .models import Store, OpeningHours


class UserSerializer(serializers.ModelSerializer):
    """
    Basic user serializer for displaying id, username and email
    """

    class Meta:
        model = User
        fields = ["id", "username", "email"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    User creation serializer allowing user to create account with
    username, email and password. Password is hashed before storage.
    """

    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]

    # enforce password hashing
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(UserCreateSerializer, self).create(validated_data)


class OpeningHoursSerializer(serializers.ModelSerializer):
    """
    Opening hours serializer including id and store_id fields.
    """

    class Meta:
        model = OpeningHours
        fields = [
            "id",
            "store_id",
            "day_of_week",
            "opening_time",
            "closing_time",
        ]


class BasicOpeningHoursSerializer(serializers.ModelSerializer):
    """
    Opening hours serializer excluding id and store_id fields.
    """

    class Meta:
        model = OpeningHours
        fields = [
            "day_of_week",
            "opening_time",
            "closing_time",
        ]


class StoreSerializer(serializers.ModelSerializer):
    """
    Store serializer with opening hours field as OpeningHoursSerializer
    field.
    """

    opening_hours = BasicOpeningHoursSerializer(
        many=True, read_only=True, source="opening_times"
    )

    class Meta:
        model = Store
        fields = ["id", "store_name", "store_address", "opening_hours"]
