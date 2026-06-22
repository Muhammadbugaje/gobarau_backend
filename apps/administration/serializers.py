from rest_framework import serializers
from apps.administration.models import (
    AcademicSession, Campus, ClassLevel, Department,
    GradingBand, GradingScale, SchoolSettings, Term, Wing
)


class SchoolSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolSettings
        fields = "__all__"
class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = "__all__"
class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = "__all__"
class WingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wing
        fields = "__all__"
class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
class ClassLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = "__all__"
class GradingScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradingScale
        fields = "__all__"
class GradingBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradingBand
        fields = "__all__"