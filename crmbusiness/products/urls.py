from django.urls import path

from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("new/", ProductCreateView.as_view(), name="products-create"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="products-delete"),
    path("<int:pk>", ProductDetailView.as_view(), name="products-detail"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="products-edit"),
]
