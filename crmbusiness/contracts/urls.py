from django.urls import path

from .views import (
    ContractCreateView,
    ContractDeleteView,
    ContractDetailView,
    ContractListView,
    ContractUpdateView,
)

app_name = "contracts"

urlpatterns = [
    path("", ContractListView.as_view(), name="contracts-list"),
    path("new/", ContractCreateView.as_view(), name="contracts-create"),
    path("<int:pk>/delete/", ContractDeleteView.as_view(), name="contracts-delete"),
    path("<int:pk>", ContractDetailView.as_view(), name="contracts-detail"),
    path("<int:pk>/edit/", ContractUpdateView.as_view(), name="contracts-edit"),
]
