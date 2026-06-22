from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.structure import Class
from apps.academics.serializers.structure import ClassSerializer
from core.permissions import IsAdminLevel, IsStaffOrAdmin

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]