from django import forms

from .models import Advertising


class AdvertisingForm(forms.ModelForm):
    class Meta:
        model = Advertising
        fields = ['name', 'product', 'promotion_channel', 'budget']
        labels = {
            'name': 'Название',
            'product': 'Рекламируемая услуга',
            'promotion_channel': 'Каналы продвижения',
            'budget': 'Бюджет (руб.)',
        }
        widgets = {
            'promotion_channel': forms.CheckboxSelectMultiple(attrs={'style': 'margin-left: 20px'}),
        }
