from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True, null=False)
    featured = models.BooleanField(default=False)  # null=True, default=True/False

    def get_absolute_url(self):
        return reverse('products:dynamic', kwargs={'my_id': self.id})  #f"/dynamic/{self.id}/"
