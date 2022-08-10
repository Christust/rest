from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.
def api_home(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    return JsonResponse({"message": "hi"})