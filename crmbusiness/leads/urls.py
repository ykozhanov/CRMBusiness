from django.urls import path

from .views import (
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadListView,
    LeadUpdateView,
)

app_name = "leads"

urlpatterns = [
    path("", LeadListView.as_view(), name="leads-list"),
    path("new/", LeadCreateView.as_view(), name="leads-create"),
    path("<int:pk>/delete/", LeadDeleteView.as_view(), name="leads-delete"),
    path("<int:pk>", LeadDetailView.as_view(), name="leads-detail"),
    path("<int:pk>/edit/", LeadUpdateView.as_view(), name="leads-edit"),
]
