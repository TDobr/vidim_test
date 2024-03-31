# Create your views here.

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from dbVisualisatorApp.api.open_trip_map_service import get_autosuggest
from dbVisualisatorApp.repository.product_repo import *
from dbVisualisatorApp.serializers import ProductSerializer


@api_view(['GET', 'POST', 'DELETE'])
def product_list_operations(request):
    if request.method == 'GET':
        all_products = get_all_products()
        serializer = ProductSerializer(all_products, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = ProductSerializer(data=request_data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return JsonResponse(serializer.to_representation(saved_data), status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        Product.objects.all().delete()
        return HttpResponse(status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'PUT', 'DELETE'])
def product_by_id_operations(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=request_data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return JsonResponse(serializer.to_representation(saved_data), status=status.HTTP_202_ACCEPTED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def open_trip_map_operations(request):
    params = request.GET.dict()

    suggestions = get_autosuggest(params.get("lat"), params.get("lon"), params.get("name"),
                                  "ru", params.get("amount"), params.get("rad"))

    return JsonResponse(suggestions, safe=False)
