from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from ads.models import Advertising
from leads.models import Lead
from products.models import Product


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["products_count"] = Product.objects.count()
        context["advertisements_count"] = Advertising.objects.count()
        context["leads_count"] = Lead.objects.filter(customer=None).count()
        context["customers_count"] = Lead.objects.filter(customer=True).count()

        return context
