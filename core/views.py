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

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all().order_by('created_at')
    serializer_class = BillSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class ImageUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        try:
            image_file = request.FILES.get('image')
            
            if not image_file:
                return Response({"error": "No image file provided."}, status=status.HTTP_400_BAD_REQUEST)
            
            processed_data = process_image_with_ai(image_file)

            bill_data = {
                'splitter_name': processed_data['splitter_name'],
                'total_price': processed_data['total_price'],
                'tax_amount': processed_data['tax_amount'],
                'service_fee': processed_data['service_fee'],
                'is_paid': False, # Default to false for a new bill
            }
            
            bill = Bill.objects.create(**bill_data)

            for item in processed_data['items']:
                BillItem.objects.create(
                    Bill=bill, **item
                )

            serializer = BillSerializer(bill)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)