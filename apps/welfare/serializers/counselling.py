from rest_framework import serializers
from apps.welfare.models.counselling import CounsellingSession

class CounsellingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellingSession
        fields = "__all__"