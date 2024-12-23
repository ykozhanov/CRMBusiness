from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products:products-list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:products-list')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-edit.html'
    success_url = reverse_lazy('products:products-list')
