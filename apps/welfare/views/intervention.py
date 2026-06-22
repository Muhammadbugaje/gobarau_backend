from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.welfare.models.intervention import InterventionCase, InterventionNote, Absence, WelfareReport
from apps.welfare.serializers.intervention import InterventionCaseSerializer, InterventionNoteSerializer, AbsenceSerializer, WelfareReportSerializer
from core.permissions import IsAdminLevel


class InterventionCaseViewSet(viewsets.ModelViewSet):
    queryset = InterventionCase.objects.all()
    serializer_class = InterventionCaseSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class InterventionNoteViewSet(viewsets.ModelViewSet):
    queryset = InterventionNote.objects.all()
    serializer_class = InterventionNoteSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class WelfareReportViewSet(viewsets.ModelViewSet):
    queryset = WelfareReport.objects.all()
    serializer_class = WelfareReportSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]