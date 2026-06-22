from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.administration.models import (
    AcademicSession, Campus, ClassLevel, Department,
    GradingBand, GradingScale, SchoolSettings, Term, Wing
)
from apps.administration.serializers import (
    AcademicSessionSerializer, CampusSerializer, ClassLevelSerializer,
    DepartmentSerializer, GradingBandSerializer, GradingScaleSerializer,
    SchoolSettingsSerializer, TermSerializer, WingSerializer
)
from core.permissions import IsAdminLevel


class SchoolSettingsViewSet(viewsets.ModelViewSet):
    queryset = SchoolSettings.objects.all()
    serializer_class = SchoolSettingsSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class AcademicSessionViewSet(viewsets.ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class WingViewSet(viewsets.ModelViewSet):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]

class ClassLevelViewSet(viewsets.ModelViewSet):
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class GradingScaleViewSet(viewsets.ModelViewSet):
    queryset = GradingScale.objects.all()
    serializer_class = GradingScaleSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]


class GradingBandViewSet(viewsets.ModelViewSet):
    queryset = GradingBand.objects.all()
    serializer_class = GradingBandSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]