from rest_framework.routers import DefaultRouter
from apps.administration.views import (
    AcademicSessionViewSet, CampusViewSet, ClassLevelViewSet,
    DepartmentViewSet, GradingBandViewSet, GradingScaleViewSet,
    SchoolSettingsViewSet, TermViewSet, WingViewSet
)

router = DefaultRouter()
router.register(r"school-settings", SchoolSettingsViewSet, basename="school-settings")
router.register(r"academic-sessions", AcademicSessionViewSet, basename="academic-session")
router.register(r"terms", TermViewSet, basename="term")
router.register(r"wings", WingViewSet, basename="wing")
router.register(r"campuses", CampusViewSet, basename="campus")
router.register(r"departments", DepartmentViewSet, basename="department")
router.register(r"class-levels", ClassLevelViewSet, basename="class-level")
router.register(r"grading-scales", GradingScaleViewSet, basename="grading-scale")
router.register(r"grading-bands", GradingBandViewSet, basename="grading-band")
urlpatterns = router.urls