from django.urls import path
from .views import HomePageView, AboutPageView, quote, categorical_quote, check_status, search_quote

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('quote/<request_category>', categorical_quote, name='categorical_quote'),
    path('quote/<request_category>/', categorical_quote, name='categorical_quote'),
    path('quote/', quote, name='quote'),
    path('search/<query>', search_quote, name='search'),
    path('', HomePageView.as_view(), name='home'),
    path('check/', check_status, name='check'),
]
