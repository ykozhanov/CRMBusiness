from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

from products.models import Product


class Contract(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='contracts', null=True)
    document = models.FileField(upload_to='contracts')
    start_date = models.DateField()
    end_date = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError('Дата начала не может быть позже даты окончания.')
