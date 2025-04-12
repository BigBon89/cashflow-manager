from datetime import datetime

from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = ChainedForeignKey(
        Category,
        chained_field="type",
        chained_model_field="type",
        on_delete=models.CASCADE,
    )
    subcategory = ChainedForeignKey(
        Subcategory,
        chained_field="category",
        chained_model_field="category",
        on_delete=models.CASCADE,
    )
    amount = models.FloatField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} {self.amount}"

    def save(self, *args, **kwargs):
        if not self.date:
            self.date = datetime.now().date()
        super().save(*args, **kwargs)
