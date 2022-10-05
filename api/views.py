from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
    return Response(data)
