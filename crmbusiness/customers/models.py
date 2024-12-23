from django.db import models
from leads.models import Lead
from  contracts.models import Contract


class Customer(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='customer')
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f'{self.lead.last_name} {self.lead.first_name}'