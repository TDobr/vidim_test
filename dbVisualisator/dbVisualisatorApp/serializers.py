import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from dbVisualisatorApp.models import Product


class ProductModel:
    def __init__(self, name, amount, created_at, updated_at, deleted):
        self.name = name
        self.amount = amount
        self.created_at = created_at
        self.updatedAt = updated_at
        self.deleted = deleted


class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False, allow_null=False)
    amount = serializers.IntegerField(required=False, allow_null=False)
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    deleted = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.deleted = validated_data.get('deleted', instance.deleted)
        instance.save()
        return instance


def encode(model):
    model_ser = ProductSerializer(model)
    return JSONRenderer().render(model_ser.data)


def decode(body):
    stream = io.BytesIO(body)
    data = JSONParser().parse(stream)
    serializer = ProductSerializer(data=data)
    serializer.is_valid()
    return serializer.validated_data
