from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.attendance import AttendanceRecord, AttendanceSummary
from apps.academics.serializers.attendance import AttendanceRecordSerializer, AttendanceSummarySerializer
from core.permissions import IsStaffOrAdmin

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class AttendanceSummaryViewSet(viewsets.ModelViewSet):
    queryset = AttendanceSummary.objects.all()
    serializer_class = AttendanceSummarySerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]