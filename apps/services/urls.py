from rest_framework.routers import DefaultRouter
from apps.services.views import (
    BookViewSet, BorrowRecordViewSet, LibraryFineViewSet,
    BusRouteViewSet, BusVehicleViewSet, TransportSubscriptionViewSet
)


router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'borrow-records', BorrowRecordViewSet, basename='borrow-record')
router.register(r'library-fines', LibraryFineViewSet, basename='library-fine')
router.register(r'bus-routes', BusRouteViewSet, basename='bus-route')
router.register(r'bus-vehicles', BusVehicleViewSet, basename='bus-vehicle')
router.register(r'transport-subscriptions', TransportSubscriptionViewSet, basename='transport-subscription')

urlpatterns = router.urls