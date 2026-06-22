from rest_framework import serializers
from apps.academics.models.attendance import AttendanceRecord, AttendanceSummary

class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = "__all__"

class AttendanceSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceSummary
        fields = "__all__"