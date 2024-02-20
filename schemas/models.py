from django.db import models
import string
import random

# Create your models here.

class BaseModel(models.Model):
    id = models.CharField(primary_key = True, max_length = 10, unique = True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child_categories')

    def __str__(self):
        self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = '2' + ''.join(random.choices(string.digits, k=9))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = '1' + ''.join(random.choices(string.digits, k=9))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
