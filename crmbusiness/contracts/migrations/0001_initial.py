# Generated by Django 5.1.4 on 2024-12-24 11:46

import datetime

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
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
                ("name", models.CharField(max_length=100)),
                ("document", models.FileField(upload_to="contracts")),
                ("start_date", models.DateField()),
                (
                    "end_date",
                    models.DateField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                datetime.date(2024, 12, 24)
                            )
                        ]
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.01)],
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contracts",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
