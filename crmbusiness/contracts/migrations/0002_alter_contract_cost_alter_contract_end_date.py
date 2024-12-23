# Generated by Django 5.1.4 on 2024-12-23 10:56

import datetime

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contracts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="cost",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0.01)],
            ),
        ),
        migrations.AlterField(
            model_name="contract",
            name="end_date",
            field=models.DateField(
                validators=[
                    django.core.validators.MinValueValidator(
                        datetime.date(2024, 12, 23)
                    )
                ]
            ),
        ),
    ]
