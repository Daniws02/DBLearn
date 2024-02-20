from django.db import models
import string
import random

# Create your models here.

class BaseModel(models.Model):
    id = models.CharField(primary_key = True, max_length = 10, unique = True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Category(BaseModel):

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = '2' + ''.join(random.choices(string.digits, k=9))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(BaseModel):
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = '1' + ''.join(random.choices(string.digits, k=9))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
