from django.shortcuts import render
from django.http import JsonResponse
from provider.models import customer
from int.models import inter
from .models import seller, customer, inter
import json
from order.models import Order


def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        buyer = customer.objects.get(name=data['buyer_name'])


        provider = seller.objects.get(code=data['discount_code'])




