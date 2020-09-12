from django.urls import path
from .views import HomePageView, AboutPageView, quote

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('quote/', quote, name='quote'),
    path('', HomePageView.as_view(), name='home'),
]
