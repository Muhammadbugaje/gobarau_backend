from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.finance.models import (
    FeeType, FeeStructure, Payment, ScholarshipFund, ScholarshipRecipient,
    ItemCategory, MarketplaceItem, MarketplaceRequest, RequestItem, RestockLog
)


@admin.register(FeeType)
class FeeTypeAdmin(ModelAdmin):
    list_display = ('name', 'code', 'is_recurring')
    list_filter = ('is_recurring',)
    search_fields = ('name', 'code', 'description')

@admin.register(FeeStructure)
class FeeStructureAdmin(ModelAdmin):
    list_display = ('fee_type', 'class_level', 'session', 'amount', 'due_date')
    list_filter = ('session', 'class_level', 'fee_type')
    search_fields = ('fee_type__name', 'class_level__name')

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    list_display = ('receipt_number', 'student', 'fee_structure', 'amount', 'payment_date', 'method', 'status')
    list_filter = ('status', 'method', 'payment_date')
    search_fields = ('receipt_number', 'student__user__username', 'reference')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(ScholarshipFund)
class ScholarshipFundAdmin(ModelAdmin):
    list_display = ('name', 'session', 'amount', 'is_active')
    list_filter = ('is_active', 'session')
    search_fields = ('name', 'description')

@admin.register(ScholarshipRecipient)
class ScholarshipRecipientAdmin(ModelAdmin):
    list_display = ('student', 'scholarship', 'amount_awarded', 'awarded_date')
    list_filter = ('awarded_date', 'scholarship')
    search_fields = ('student__user__username', 'scholarship__name')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(ItemCategory)
class ItemCategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')

@admin.register(MarketplaceItem)
class MarketplaceItemAdmin(ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_available')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'description')

@admin.register(MarketplaceRequest)
class MarketplaceRequestAdmin(ModelAdmin):
    list_display = ('student', 'request_date', 'status')
    list_filter = ('status', 'request_date')
    search_fields = ('student__user__username',)

@admin.register(RequestItem)
class RequestItemAdmin(ModelAdmin):
    list_display = ('request', 'item', 'quantity', 'unit_price')
    search_fields = ('item__name',)

@admin.register(RestockLog)
class RestockLogAdmin(ModelAdmin):
    list_display = ('item', 'quantity_added', 'previous_stock', 'new_stock', 'restocked_at')
    list_filter = ('restocked_at',)
    search_fields = ('item__name',)
    readonly_fields = ('restocked_at', 'created_at', 'updated_at', 'created_by', 'updated_by')