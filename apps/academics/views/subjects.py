from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.academics.models.subjects import Subject, TeacherClassSubject
from apps.academics.serializers.subjects import SubjectSerializer, TeacherClassSubjectSerializer
from core.permissions import IsAdminLevel, IsStaffOrAdmin

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class TeacherClassSubjectViewSet(viewsets.ModelViewSet):
    queryset = TeacherClassSubject.objects.all()
    serializer_class = TeacherClassSubjectSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]