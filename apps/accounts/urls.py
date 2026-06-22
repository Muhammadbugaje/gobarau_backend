from rest_framework.routers import DefaultRouter
from apps.accounts.views import PersonViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"people", PersonViewSet, basename="person")
urlpatterns = router.urls