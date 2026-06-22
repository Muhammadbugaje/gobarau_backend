from rest_framework import serializers
from apps.communication.models import Announcement, Notification, Message, Question, CareerTalkSession

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class CareerTalkSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerTalkSession
        fields = "__all__"