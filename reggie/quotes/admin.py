from django.contrib import admin

from .models import Quotation, Category

admin.site.register(Category)
admin.site.register(Quotation)
