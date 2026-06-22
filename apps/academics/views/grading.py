from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.grading import CAConfiguration
from apps.academics.serializers.grading import CAConfigurationSerializer
from core.permissions import IsAdminLevel

class CAConfigurationViewSet(viewsets.ModelViewSet):
    queryset = CAConfiguration.objects.all()
    serializer_class = CAConfigurationSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]