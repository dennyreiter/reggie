from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
import django.views.debug
from django.forms.models import model_to_dict
from .models import Quotation, Category
import random

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def check_status(request):
    data = get_traceback_data()
    return JsonResponse(data)

def quote(request):
    items = Quotation.objects.all()
    random_item = random.choice(items)
    random_item.count += 1
    data = {
            'category': model_to_dict(random_item.category),
            'quote': random_item.quote,
            'created': random_item.created,
            'last_served': random_item.last_served,
            'count': random_item.count 
            }
    random_item.save()
    return JsonResponse(data)

def categorical_quote(request, request_category):
    items = Quotation.objects.filter(category__name=request_category.lower())
    if items.exists():
        random_item = random.choice(items)
        random_item.count += 1
        data = {
                'category': model_to_dict(random_item.category),
                'quote': random_item.quote,
                'created': random_item.created,
                'last_served': random_item.last_served,
                'count': random_item.count 
                }
        random_item.save()
        return JsonResponse(data)
    else:
        return redirect(quote)

def search_quote(request, query):
    items = Quotation.objects.filter(quote__icontains=query)
    datum = []
    for item in items:
        data = {
                'category': model_to_dict(item.category),
                'quote': item.quote,
                'created': item.created,
                'last_served': item.last_served,
                'count': item.count 
                }
        datum += data
    return HttpResponse(datum)

class SearchView(ListView):
    template_name = 'search.html'
    paginate_by = 10
    count = 0
