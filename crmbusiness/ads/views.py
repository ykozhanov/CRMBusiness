from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, DecimalField, ExpressionWrapper, F, Q, Sum
from django.db.models.functions import Round
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AdvertisingForm
from .models import Advertising


class AdvertisingListView(LoginRequiredMixin, ListView):
    model = Advertising
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdvertisingCreateView(LoginRequiredMixin, CreateView):
    model = Advertising
    form_class = AdvertisingForm
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("ads:ads-list")


class AdvertisingDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertising
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy("ads:ads-list")


class AdvertisingDetailView(LoginRequiredMixin, DetailView):
    model = Advertising
    template_name = "ads/ads-detail.html"


class AdvertisingUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertising
    form_class = AdvertisingForm
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy("ads:ads-list")


class StatisticListView(LoginRequiredMixin, ListView):
    model = Advertising
    queryset = Advertising.objects.annotate(
        leads_count=Count("leads", filter=Q(leads__customer__isnull=True)),
        customers_count=Count(
            "leads__customer", filter=Q(leads__customer__isnull=False)
        ),
        profit=Round(
            ExpressionWrapper(
                (Sum("product__contracts__cost", distinct=True) - F("budget")),
                output_field=DecimalField(),
            )
        ),
    )
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"
