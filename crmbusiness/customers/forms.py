from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contract', 'lead']
        labels = {
            'contract': 'Договор',
            'lead': 'Лид',
        }
