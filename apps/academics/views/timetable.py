from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.timetable import Timetable, ExamTimetable
from apps.academics.serializers.timetable import TimetableSerializer, ExamTimetableSerializer
from core.permissions import IsStaffOrAdmin

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class ExamTimetableViewSet(viewsets.ModelViewSet):
    queryset = ExamTimetable.objects.all()
    serializer_class = ExamTimetableSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]