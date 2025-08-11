from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Bill, BillItem
from .serializers import BillSerializer

def process_image_with_ai (image_file):
    
    print("Processing image with AI...")

    return {
        "splitter_name": "Lunch with Friends",
        "total_price": 55.75,
        "tax_amount": 4.50,
        "service_fee": 5.00,
        "items": [
            {"item_name": "Burger", "price": 12.50},
            {"item_name": "Fries", "price": 5.25},
            {"item_name": "Coke", "price": 3.00},
            {"item_name": "Salad", "price": 15.00},
            {"item_name": "Pizza", "price": 15.00},
        ]
    }

# Create your views here.
