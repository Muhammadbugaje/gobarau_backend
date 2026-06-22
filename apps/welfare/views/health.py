from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.welfare.models.health import HealthProfile, ClinicVisit, Medication
from apps.welfare.serializers.health import HealthProfileSerializer, ClinicVisitSerializer, MedicationSerializer
from apps.welfare.permissions import IsSchoolNurse


class HealthProfileViewSet(viewsets.ModelViewSet):
    queryset = HealthProfile.objects.all()
    serializer_class = HealthProfileSerializer
    permission_classes = [IsAuthenticated, IsSchoolNurse]

class ClinicVisitViewSet(viewsets.ModelViewSet):
    queryset = ClinicVisit.objects.all()
    serializer_class = ClinicVisitSerializer
    permission_classes = [IsAuthenticated, IsSchoolNurse]

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, IsSchoolNurse]