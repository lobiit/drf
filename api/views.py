from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # is_instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
