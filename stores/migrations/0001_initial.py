# Generated by Django 4.2 on 2023-04-13 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store_name", models.CharField(max_length=100)),
                ("store_address", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="OpeningHours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day_of_week",
                    models.CharField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        max_length=10,
                    ),
                ),
                ("opening_time", models.TimeField()),
                ("closing_time", models.TimeField()),
                (
                    "store_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stores.store"
                    ),
                ),
            ],
        ),
    ]
