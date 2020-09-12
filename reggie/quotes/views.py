from django.shortcuts import render
#from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def quote(request):
    data = {
            'category': 'Random',
            'quote': 'Wherever you go, there you are',
            'created': '1968/12/18',
            'last_served': '2020/09/10 19:20:21',
            'count': 77
            }
    return JsonResponse(data)
