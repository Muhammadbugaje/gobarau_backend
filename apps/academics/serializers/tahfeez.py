from rest_framework import serializers
from apps.academics.models.tahfeez import JuzProgress, RecitationSession

class JuzProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = JuzProgress
        fields = "__all__"

class RecitationSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecitationSession
        fields = "__all__"