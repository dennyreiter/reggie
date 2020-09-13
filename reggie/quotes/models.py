from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Quotation(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quote = models.CharField(max_length=400)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    last_served = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Quotations"

    def __str__(self):
        return self.quote

