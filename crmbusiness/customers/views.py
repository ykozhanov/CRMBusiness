from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import CustomerForm
from .models import Customer


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"
    permission_required = "customers.view_customer"


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.add_customer"


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.delete_customer"


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customers-detail.html"
    permission_required = "customers.view_customer"


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy("customers:customers-list")
    permission_required = "customers.change_customer"
