import uuid

from django.db import models

from dbVisualisatorApp.dto.product_dtos import CreateProductDto


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampMixin(Base):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampMixin):
    name = models.CharField(unique=True, max_length=200, blank=False)
    amount = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    # def __init__(self, name, amount):
    #     self.name = name
    #     self.amount = amount


class Shop(TimeStampMixin):
    name = models.CharField(max_length=200, blank=False)
    product_amount = models.IntegerField(default=0)
    products = models.JSONField()


def convert_to_products_model(dto: CreateProductDto):
    return Product(dto.name, dto.amount)
