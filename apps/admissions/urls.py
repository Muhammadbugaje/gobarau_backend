from rest_framework.routers import DefaultRouter
from apps.admissions.views import ApplicationViewSet, EntranceExamViewSet, AlumniRegistrationViewSet

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'entrance-exams', EntranceExamViewSet, basename='entrance-exam')
router.register(r'alumni-registrations', AlumniRegistrationViewSet, basename='alumni-registration')

urlpatterns = router.urls