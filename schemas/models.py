from django.db import models
import string
import random

# Create your models here.

class Product(models.Model):
    id = models.CharField(primary_key = True, max_length = 10, unique = True)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = '1' + ''.join(random.choices(string.digits, k=9))
        super().save(*args, **kwargs)