from rest_framework import serializers
from apps.academics.models.grading import CAConfiguration

class CAConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CAConfiguration
        fields = "__all__"