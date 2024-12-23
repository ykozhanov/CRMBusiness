from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Customer
from .forms import CustomerForm


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'
    success_url = reverse_lazy('customers:customers-list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('customers:customers-list')


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-edit.html'
    success_url = reverse_lazy('customers:customers-list')
