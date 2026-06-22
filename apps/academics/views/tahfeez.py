from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.tahfeez import JuzProgress, RecitationSession
from apps.academics.serializers.tahfeez import JuzProgressSerializer, RecitationSessionSerializer
from core.permissions import IsStaffOrAdmin

class JuzProgressViewSet(viewsets.ModelViewSet):
    queryset = JuzProgress.objects.all()
    serializer_class = JuzProgressSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class RecitationSessionViewSet(viewsets.ModelViewSet):
    queryset = RecitationSession.objects.all()
    serializer_class = RecitationSessionSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]