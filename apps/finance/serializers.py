from rest_framework import serializers
from apps.finance.models import (
    FeeType, FeeStructure, Payment, ScholarshipFund, ScholarshipRecipient,
    ItemCategory, MarketplaceItem, MarketplaceRequest, RequestItem, RestockLog
)

class FeeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeType
        fields = "__all__"
        
class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = "__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        
class ScholarshipFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipFund
        fields = "__all__"
        
class ScholarshipRecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipRecipient
        fields = "__all__"
        
class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = "__all__"
        
class MarketplaceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceItem
        fields = "__all__"
        
class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = "__all__"
        
class MarketplaceRequestSerializer(serializers.ModelSerializer):
    request_items = RequestItemSerializer(many=True, read_only=True)
    class Meta:
        model = MarketplaceRequest
        fields = "__all__"
        
class RestockLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestockLog
        fields = "__all__"