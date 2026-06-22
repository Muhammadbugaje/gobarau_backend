from rest_framework.routers import DefaultRouter
from apps.academics.views import (
    ClassViewSet, SubjectViewSet, TeacherClassSubjectViewSet, CAConfigurationViewSet,
    TimetableViewSet, ExamTimetableViewSet, ScoreViewSet, ReportCardViewSet,
    AssignmentViewSet, AssignmentSubmissionViewSet, AttendanceRecordViewSet,
    AttendanceSummaryViewSet, ExamRegistrationViewSet, ExamResultViewSet,
    JuzProgressViewSet, RecitationSessionViewSet
)

router = DefaultRouter()
router.register(r"classes", ClassViewSet, basename="class")
router.register(r"subjects", SubjectViewSet, basename="subject")
router.register(r"teacher-class-subjects", TeacherClassSubjectViewSet, basename="teacher-class-subject")
router.register(r"ca-configurations", CAConfigurationViewSet, basename="ca-configuration")
router.register(r"timetables", TimetableViewSet, basename="timetable")
router.register(r"exam-timetables", ExamTimetableViewSet, basename="exam-timetable")
router.register(r"scores", ScoreViewSet, basename="score")
router.register(r"report-cards", ReportCardViewSet, basename="report-card")
router.register(r"assignments", AssignmentViewSet, basename="assignment")
router.register(r"assignment-submissions", AssignmentSubmissionViewSet, basename="assignment-submission")
router.register(r"attendance-records", AttendanceRecordViewSet, basename="attendance-record")
router.register(r"attendance-summaries", AttendanceSummaryViewSet, basename="attendance-summary")
router.register(r"exam-registrations", ExamRegistrationViewSet, basename="exam-registration")
router.register(r"exam-results", ExamResultViewSet, basename="exam-result")
router.register(r"juz-progresses", JuzProgressViewSet, basename="juz-progress")
router.register(r"recitation-sessions", RecitationSessionViewSet, basename="recitation-session")

urlpatterns = router.urls