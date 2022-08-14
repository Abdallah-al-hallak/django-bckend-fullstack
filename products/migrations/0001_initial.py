# Generated by Django 4.0.6 on 2022-08-14 18:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('icon_url', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_categories', to='products.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.CharField(max_length=512)),
                ('immage1_url', models.URLField(blank=True, null=True)),
                ('immage2_url', models.URLField(blank=True, null=True)),
                ('immage3_url', models.URLField(blank=True, null=True)),
                ('immage4_url', models.URLField(blank=True, null=True)),
                ('prince', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('SEK', 'Swedish Crown'), ('USD', 'American Dollar'), ('EUR', 'Euro')], default='USD', max_length=3)),
                ('variation_product_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
                ('maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.maker')),
            ],
        ),
    ]
