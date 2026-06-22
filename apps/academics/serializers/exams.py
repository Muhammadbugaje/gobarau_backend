from rest_framework import serializers
from apps.academics.models.exams import ExamRegistration, ExamResult

class ExamRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamRegistration
        fields = "__all__"

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = "__all__"