# Generated by Django 3.1.1 on 2020-09-13 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20200913_0119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'verbose_name_plural': 'Quotations'},
        ),
        migrations.AddField(
            model_name='quotation',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quotation',
            name='last_served',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
