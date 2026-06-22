from rest_framework import serializers
from apps.academics.models.timetable import Timetable, ExamTimetable

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = "__all__"

class ExamTimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTimetable
        fields = "__all__"