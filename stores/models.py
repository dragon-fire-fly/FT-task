from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    """
    Store model with name and address fields.
    """

    store_name = models.CharField(max_length=100, unique=True)
    store_address = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Store: {self.store_name}"


class OpeningHours(models.Model):
    """
    Opening hours model, related to store through store_id foreign key.
    """

    store_id = models.ForeignKey(
        Store, related_name="opening_times", on_delete=models.CASCADE
    )
    day_of_week = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        unique_together = ["store_id", "day_of_week"]

    def __str__(self):
        return f"Opening hours for {self.day_of_week}: {self.opening_time} til {self.closing_time}"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
