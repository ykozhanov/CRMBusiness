from django.db import models

from ads.models import Advertising


class Lead(models.Model):
    last_name = models.CharField(max_length=100, null=False)
    first_name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    advertising = models.ForeignKey(
        Advertising, on_delete=models.SET_NULL, related_name="leads", null=True
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
