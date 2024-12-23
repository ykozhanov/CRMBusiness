from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .views import ProfileTemplateView

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileTemplateView.as_view(), name='users-index'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('users:login')), name='logout'),
]
