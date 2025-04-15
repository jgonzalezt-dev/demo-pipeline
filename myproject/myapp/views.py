from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
from django.http import JsonResponse

def ping(request):
    return JsonResponse({'ping': 'pong', 
                         'date': datetime.now().isoformat()})


