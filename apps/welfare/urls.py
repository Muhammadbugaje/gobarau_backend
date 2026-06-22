from rest_framework.routers import DefaultRouter
from apps.welfare.views import (
    HealthProfileViewSet, ClinicVisitViewSet, MedicationViewSet,
    CounsellingSessionViewSet, DisciplinaryRecordViewSet, MeritDeductionViewSet,
    InterventionCaseViewSet, InterventionNoteViewSet, AbsenceViewSet, WelfareReportViewSet
)


router = DefaultRouter()
router.register(r'health-profiles', HealthProfileViewSet, basename='health-profile')
router.register(r'clinic-visits', ClinicVisitViewSet, basename='clinic-visit')
router.register(r'medications', MedicationViewSet, basename='medication')
router.register(r'counselling-sessions', CounsellingSessionViewSet, basename='counselling-session')
router.register(r'disciplinary-records', DisciplinaryRecordViewSet, basename='disciplinary-record')
router.register(r'merit-deductions', MeritDeductionViewSet, basename='merit-deduction')
router.register(r'intervention-cases', InterventionCaseViewSet, basename='intervention-case')
router.register(r'intervention-notes', InterventionNoteViewSet, basename='intervention-note')
router.register(r'absences', AbsenceViewSet, basename='absence')
router.register(r'welfare-reports', WelfareReportViewSet, basename='welfare-report')

urlpatterns = router.urls