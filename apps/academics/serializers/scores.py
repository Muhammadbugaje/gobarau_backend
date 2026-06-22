from rest_framework import serializers
from apps.academics.models.scores import Score, ReportCard, Assignment, AssignmentSubmission

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"

class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = "__all__"

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = "__all__"