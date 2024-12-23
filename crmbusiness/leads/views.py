from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Lead
from .forms import LeadForm


class LeadListView(ListView):
    model = Lead
    queryset = Lead.objects.filter(customer=None)
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-create.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:leads-list')


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-edit.html'
    success_url = reverse_lazy('leads:leads-list')
