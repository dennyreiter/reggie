from django.shortcuts import render
#from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.forms.models import model_to_dict
from .models import Quotation, Category
import random

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def quote(request):
    items = Quotation.objects.all()
    random_item = random.choice(items)
    random_item.count += 1
    random_item.save()
    data = {
            'category': model_to_dict(random_item.category),
            'quote': random_item.quote,
            'created': random_item.created,
            'last_served': random_item.last_served,
            'count': random_item.count 
            }
    return JsonResponse(data)

def categorical_quote(request, request_category):
    items = Quotation.objects.filter(category__name=request_category)
    random_item = random.choice(items)
    random_item.count += 1
    random_item.save()
    data = {
            'category': model_to_dict(random_item.category),
            'quote': random_item.quote,
            'created': random_item.created,
            'last_served': random_item.last_served,
            'count': random_item.count 
            }
    return JsonResponse(data)
