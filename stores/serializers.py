from rest_framework import serializers
from .models import Store, OpeningHours


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


class StoreSerializer(serializers.ModelSerializer):
    """
    Store serializer with opening hours field as OpeningHoursSerializer
    field.
    """

    opening_hours = OpeningHoursSerializer(
        many=True, read_only=True, source="opening_times"
    )

    class Meta:
        model = Store
        fields = ["id", "store_name", "store_address", "opening_hours"]
