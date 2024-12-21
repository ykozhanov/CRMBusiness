from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost']
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'cost': 'Стоимость (руб.)',
        }