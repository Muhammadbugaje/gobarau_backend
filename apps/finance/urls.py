from rest_framework.routers import DefaultRouter
from apps.finance.views import (
    FeeTypeViewSet, FeeStructureViewSet, PaymentViewSet, ScholarshipFundViewSet,
    ScholarshipRecipientViewSet, ItemCategoryViewSet, MarketplaceItemViewSet,
    MarketplaceRequestViewSet, RequestItemViewSet, RestockLogViewSet
)

router = DefaultRouter()
router.register(r'fee-types', FeeTypeViewSet, basename='fee-type')
router.register(r'fee-structures', FeeStructureViewSet, basename='fee-structure')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'scholarship-funds', ScholarshipFundViewSet, basename='scholarship-fund')
router.register(r'scholarship-recipients', ScholarshipRecipientViewSet, basename='scholarship-recipient')
router.register(r'item-categories', ItemCategoryViewSet, basename='item-category')
router.register(r'marketplace-items', MarketplaceItemViewSet, basename='marketplace-item')
router.register(r'marketplace-requests', MarketplaceRequestViewSet, basename='marketplace-request')
router.register(r'request-items', RequestItemViewSet, basename='request-item')
router.register(r'restock-logs', RestockLogViewSet, basename='restock-log')
urlpatterns = router.urls