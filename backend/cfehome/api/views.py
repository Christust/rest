from django.http import JsonResponse
import json
from django.forms import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)