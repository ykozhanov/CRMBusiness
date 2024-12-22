from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'phone', 'email', 'advertising']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'phone': 'Номер телефона',
            'email': 'E-mail',
            'advertising': 'Рекламная кампания',
        }
