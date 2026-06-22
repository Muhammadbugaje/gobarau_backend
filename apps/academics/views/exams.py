from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.exams import ExamRegistration, ExamResult
from apps.academics.serializers.exams import ExamRegistrationSerializer, ExamResultSerializer
from core.permissions import IsStaffOrAdmin, IsAdminLevel

class ExamRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ExamRegistration.objects.all()
    serializer_class = ExamRegistrationSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]