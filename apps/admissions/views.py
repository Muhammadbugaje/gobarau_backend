from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.admissions.models import Application, EntranceExam, AlumniRegistration
from apps.admissions.serializers import ApplicationSerializer, EntranceExamSerializer, AlumniRegistrationSerializer
from core.permissions import IsAdminLevel, IsStaffOrAdmin

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class EntranceExamViewSet(viewsets.ModelViewSet):
    queryset = EntranceExam.objects.all()
    serializer_class = EntranceExamSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class AlumniRegistrationViewSet(viewsets.ModelViewSet):
    queryset = AlumniRegistration.objects.all()
    serializer_class = AlumniRegistrationSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]