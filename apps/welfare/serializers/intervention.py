from rest_framework import serializers
from apps.welfare.models.intervention import InterventionCase, InterventionNote, Absence, WelfareReport


class InterventionCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterventionCase
        fields = "__all__"

class InterventionNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterventionNote
        fields = "__all__"

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = "__all__"

class WelfareReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelfareReport
        fields = "__all__"