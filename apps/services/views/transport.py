from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.services.models.transport import BusRoute, BusVehicle, TransportSubscription
from apps.services.serializers.transport import BusRouteSerializer, BusVehicleSerializer, TransportSubscriptionSerializer
from core.permissions import IsStaffOrAdmin


class BusRouteViewSet(viewsets.ModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class BusVehicleViewSet(viewsets.ModelViewSet):
    queryset = BusVehicle.objects.all()
    serializer_class = BusVehicleSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class TransportSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = TransportSubscription.objects.all()
    serializer_class = TransportSubscriptionSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]