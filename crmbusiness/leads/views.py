from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import LeadForm
from .models import Lead


class LeadListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Lead
    queryset = Lead.objects.filter(customer=None)
    template_name = "leads/leads-list.html"
    context_object_name = "leads"
    permission_required = "leads.view_lead"


class LeadCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-create.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.add_lead"


class LeadDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Lead
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.delete_lead"


class LeadDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/leads-detail.html"
    permission_required = "leads.view_lead"


class LeadUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy("leads:leads-list")
    permission_required = "leads.change_lead"
