from rest_framework import serializers
from apps.services.models.transport import BusRoute, BusVehicle, TransportSubscription


class BusRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusRoute
        fields = "__all__"

class BusVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusVehicle
        fields = "__all__"

class TransportSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportSubscription
        fields = "__all__"