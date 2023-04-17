from django.db import models

DAYS_OF_WEEK = [
    ("mon", "Monday"),
    ("tues", "Tuesday"),
    ("weds", "Wednesday"),
    ("thurs", "Thursday"),
    ("fri", "Friday"),
    ("sat", "Saturday"),
    ("sun", "Sunday"),
]


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=255)

    def __str__(self):
        return f"Store: {self.store_name}"


class OpeningHours(models.Model):
    store_id = models.ForeignKey(
        Store, related_name="opening_times", on_delete=models.CASCADE
    )
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
