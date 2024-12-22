from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Client
from .forms import ClientForm


class LeadListView(ListView):
    model = Client
    queryset = Client.objects.filter(status='lead')
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadDeleteView(DeleteView):
    model = Client
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadDetailView(DetailView):
    model = Client
    template_name = 'leads/leads-detail.html'


class LeadUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:leads-list')
