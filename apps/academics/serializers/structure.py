from rest_framework import serializers
from apps.academics.models.structure import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"