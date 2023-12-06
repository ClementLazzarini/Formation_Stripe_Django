from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Nom du produit")
    slug = models.SlugField(max_length=128, blank=True, unique=True)
    price = models.FloatField(default=0.0, blank=True, verbose_name="Prix du produit")
    thumbnail = models.ImageField(blank=True, verbose_name="Image du produit")
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0, blank=True, verbose_name="Stock du produit")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={"slug": self.slug})


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.TextField()
    reference = models.CharField(max_length=128)
    date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, default="Créer")
    price = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return f"Order of {self.user}"
