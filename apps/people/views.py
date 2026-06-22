from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.people.models import (
    StudentProfile, TeacherProfile, ParentProfile, AlumniProfile,
    ClassEnrollment, WardRelationship
)
from apps.people.serializers import (
    StudentProfileSerializer, TeacherProfileSerializer, ParentProfileSerializer,
    AlumniProfileSerializer, ClassEnrollmentSerializer, WardRelationshipSerializer
)
from core.permissions import IsStaffOrAdmin, IsAdminLevel


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class ParentProfileViewSet(viewsets.ModelViewSet):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class AlumniProfileViewSet(viewsets.ModelViewSet):
    queryset = AlumniProfile.objects.all()
    serializer_class = AlumniProfileSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class ClassEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = ClassEnrollment.objects.all()
    serializer_class = ClassEnrollmentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]


class WardRelationshipViewSet(viewsets.ModelViewSet):
    queryset = WardRelationship.objects.all()
    serializer_class = WardRelationshipSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]