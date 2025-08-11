from rest_framework import serializers
from .models import Bill, BillItem

class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
        fields = ['id', 'item_name', 'item_price']

class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'splitter_name', 'total_price', 'tax_amount', 'service_charge', 'is_paid', 'date', 'items']
    
