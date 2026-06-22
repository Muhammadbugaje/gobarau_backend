from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.welfare.models.discipline import DisciplinaryRecord, MeritDeduction
from apps.welfare.serializers.discipline import DisciplinaryRecordSerializer, MeritDeductionSerializer
from core.permissions import IsAdminLevel


class DisciplinaryRecordViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaryRecord.objects.all()
    serializer_class = DisciplinaryRecordSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class MeritDeductionViewSet(viewsets.ModelViewSet):
    queryset = MeritDeduction.objects.all()
    serializer_class = MeritDeductionSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]