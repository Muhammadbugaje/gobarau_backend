from rest_framework.routers import DefaultRouter
from apps.people.views import (
    StudentProfileViewSet, TeacherProfileViewSet, ParentProfileViewSet,
    AlumniProfileViewSet, ClassEnrollmentViewSet, WardRelationshipViewSet
)

router = DefaultRouter()
router.register(r'students', StudentProfileViewSet, basename='student')
router.register(r'teachers', TeacherProfileViewSet, basename='teacher')
router.register(r'parents', ParentProfileViewSet, basename='parent')
router.register(r'alumni', AlumniProfileViewSet, basename='alumni')
router.register(r'enrollments', ClassEnrollmentViewSet, basename='enrollment')
router.register(r'ward-relationships', WardRelationshipViewSet, basename='ward-relationship')

urlpatterns = router.urls