from rest_framework import serializers
from apps.people.models import (
    StudentProfile, TeacherProfile, ParentProfile, AlumniProfile,
    ClassEnrollment, WardRelationship
)


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = "__all__"


class ParentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentProfile
        fields = "__all__"


class AlumniProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniProfile
        fields = "__all__"


class ClassEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassEnrollment
        fields = "__all__"


class WardRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardRelationship
        fields = "__all__"