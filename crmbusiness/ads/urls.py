from django.urls import path

from .views import AdvertisingListView, AdvertisingCreateView, AdvertisingDeleteView, AdvertisingDetailView, AdvertisingUpdateView, StatisticListView

app_name = "ads"

urlpatterns = [
    path('', AdvertisingListView.as_view(), name='ads-list'),
    path('new/', AdvertisingCreateView.as_view(), name='ads-create'),
    path('<int:pk>/delete/', AdvertisingDeleteView.as_view(), name='ads-delete'),
    path('<int:pk>', AdvertisingDetailView.as_view(), name='ads-detail'),
    path('<int:pk>/edit/', AdvertisingUpdateView.as_view(), name='ads-edit'),
    path('statistic', StatisticListView.as_view(), name='ads-statistic'),
]
