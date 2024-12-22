from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Advertising
from .forms import AdvertisingForm


class AdvertisingListView(ListView):
    model = Advertising
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdvertisingCreateView(CreateView):
    model = Advertising
    form_class = AdvertisingForm
    template_name = 'ads/ads-create.html'
    success_url = reverse_lazy('ads:ads-list')


class AdvertisingDeleteView(DeleteView):
    model = Advertising
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:ads-list')


class AdvertisingDetailView(DetailView):
    model = Advertising
    template_name = 'ads/ads-detail.html'


class AdvertisingUpdateView(UpdateView):
    model = Advertising
    form_class = AdvertisingForm
    template_name = 'ads/ads-edit.html'
    success_url = reverse_lazy('ads:ads-list')
