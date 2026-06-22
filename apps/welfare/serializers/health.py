from rest_framework import serializers
from apps.welfare.models.health import HealthProfile, ClinicVisit, Medication


class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = "__all__"

class ClinicVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicVisit
        fields = "__all__"
class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"