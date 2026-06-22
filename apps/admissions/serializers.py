from rest_framework import serializers
from apps.admissions.models import Application, EntranceExam, AlumniRegistration

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

class EntranceExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceExam
        fields = "__all__"

class AlumniRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumniRegistration
        fields = "__all__"