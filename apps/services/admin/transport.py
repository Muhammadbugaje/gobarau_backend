from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.services.models.transport import BusRoute, BusVehicle, TransportSubscription


@admin.register(BusRoute)
class BusRouteAdmin(ModelAdmin):
    list_display = ('name', 'origin', 'destination', 'distance_km')
    search_fields = ('name', 'origin', 'destination')

@admin.register(BusVehicle)
class BusVehicleAdmin(ModelAdmin):
    list_display = ('registration_number', 'capacity', 'driver', 'route')
    list_filter = ('route',)
    search_fields = ('registration_number', 'driver__user__username')

@admin.register(TransportSubscription)
class TransportSubscriptionAdmin(ModelAdmin):
    list_display = ('student', 'route', 'session', 'direction', 'fee_amount')
    list_filter = ('direction', 'session')
    search_fields = ('student__user__username', 'route__name')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')