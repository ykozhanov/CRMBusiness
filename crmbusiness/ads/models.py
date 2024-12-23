from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product


class PromotionChannel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", null=False)

    class Meta:
        verbose_name = "Канал продвижения"
        verbose_name_plural = "Каналы продвижения"

    def __str__(self):
        return self.name


class Advertising(models.Model):
    name = models.CharField(max_length=100, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    promotion_channel = models.ManyToManyField(
        PromotionChannel, related_name="advertising"
    )
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return self.name
