from django.urls import path
from coin.views import CoinApi


urlpatterns = [
    path("flip/",CoinApi.as_view())
]