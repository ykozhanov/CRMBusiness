from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Product
from .forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-create.html'
    success_url = reverse_lazy('products-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products-list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/products-edit.html'
    success_url = reverse_lazy('products-list')
