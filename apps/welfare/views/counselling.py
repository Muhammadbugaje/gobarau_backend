from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.welfare.models.counselling import CounsellingSession
from apps.welfare.serializers.counselling import CounsellingSessionSerializer
from apps.welfare.permissions import IsCounsellor


class CounsellingSessionViewSet(viewsets.ModelViewSet):
    queryset = CounsellingSession.objects.all()
    serializer_class = CounsellingSessionSerializer
    permission_classes = [IsAuthenticated, IsCounsellor]