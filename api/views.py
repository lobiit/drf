from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
