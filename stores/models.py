from django.db import models

DAYS_OF_WEEK = [
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
]


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=255)


class OpeningHours(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
