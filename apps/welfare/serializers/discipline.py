from rest_framework import serializers
from apps.welfare.models.discipline import DisciplinaryRecord, MeritDeduction


class DisciplinaryRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaryRecord
        fields = "__all__"

class MeritDeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeritDeduction
        fields = "__all__"