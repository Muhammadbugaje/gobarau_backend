from rest_framework import serializers
from apps.academics.models.subjects import Subject, TeacherClassSubject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClassSubject
        fields = "__all__"