from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as postgresFields

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish Crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        EURO = ("EUR", _("Euro"))

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=512)
    maker = models.ForeignKey(
        Maker, related_name="products", on_delete=models.CASCADE, blank=True, null=True
    )
    immage1_url = models.URLField(blank=True, null=True)
    immage2_url = models.URLField(blank=True, null=True)
    immage3_url = models.URLField(blank=True, null=True)
    immage4_url = models.URLField(blank=True, null=True)
    prince = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )
    variation_product_id = postgresFields.ArrayField(
        models.IntegerField(blank=True, null=True),
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title} - {self.subtitle} - {self.maker}"
