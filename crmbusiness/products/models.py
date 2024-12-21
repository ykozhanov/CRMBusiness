from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True, default='')
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
