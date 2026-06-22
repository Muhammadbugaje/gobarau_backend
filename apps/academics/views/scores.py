from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.scores import Score, ReportCard, Assignment, AssignmentSubmission
from apps.academics.serializers.scores import ScoreSerializer, ReportCardSerializer, AssignmentSerializer, AssignmentSubmissionSerializer
from core.permissions import IsStaffOrAdmin, IsAdminLevel, IsOwnStudent

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class ReportCardViewSet(viewsets.ModelViewSet):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]