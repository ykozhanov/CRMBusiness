from django import forms

from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["name", "product", "start_date", "end_date", "cost", "document"]
        labels = {
            "name": "Название",
            "product": "Услуга",
            "start_date": "Начальная дата",
            "end_date": "Дата окончания",
            "cost": "Сумма (руб.)",
            "document": "Договор",
        }
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }
