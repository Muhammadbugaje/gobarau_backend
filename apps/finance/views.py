from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.finance.models import (
    FeeType, FeeStructure, Payment, ScholarshipFund, ScholarshipRecipient,
    ItemCategory, MarketplaceItem, MarketplaceRequest, RequestItem, RestockLog
)

from apps.finance.serializers import (
    FeeTypeSerializer, FeeStructureSerializer, PaymentSerializer,
    ScholarshipFundSerializer, ScholarshipRecipientSerializer,
    ItemCategorySerializer, MarketplaceItemSerializer, MarketplaceRequestSerializer,
    RequestItemSerializer, RestockLogSerializer
)

from core.permissions import IsStaffOrAdmin, IsAdminLevel


class FeeTypeViewSet(viewsets.ModelViewSet):
    queryset = FeeType.objects.all()
    serializer_class = FeeTypeSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class ScholarshipFundViewSet(viewsets.ModelViewSet):
    queryset = ScholarshipFund.objects.all()
    serializer_class = ScholarshipFundSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class ScholarshipRecipientViewSet(viewsets.ModelViewSet):
    queryset = ScholarshipRecipient.objects.all()
    serializer_class = ScholarshipRecipientSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class MarketplaceItemViewSet(viewsets.ModelViewSet):
    queryset = MarketplaceItem.objects.all()
    serializer_class = MarketplaceItemSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class MarketplaceRequestViewSet(viewsets.ModelViewSet):
    queryset = MarketplaceRequest.objects.all()
    serializer_class = MarketplaceRequestSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class RequestItemViewSet(viewsets.ModelViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class RestockLogViewSet(viewsets.ModelViewSet):
    queryset = RestockLog.objects.all()
    serializer_class = RestockLogSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]