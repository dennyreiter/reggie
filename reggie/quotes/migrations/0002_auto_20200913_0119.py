# Generated by Django 3.1.1 on 2020-09-13 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='quotation',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.category'),
        ),
    ]
