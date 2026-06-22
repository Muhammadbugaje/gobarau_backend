from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.communication.models import Announcement, Notification, Message, Question, CareerTalkSession
from apps.communication.serializers import (
    AnnouncementSerializer, NotificationSerializer, MessageSerializer,
    QuestionSerializer, CareerTalkSessionSerializer
)

from core.permissions import IsStaffOrAdmin, IsAdminLevel


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Users see only their own notifications; admins see all
        user = self.request.user
        if user.is_superuser or user.role in ['super_admin', 'principal', 'vice_principal']:
            return Notification.objects.all()
        return Notification.objects.filter(recipient=user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # Users see only messages they sent or received
        user = self.request.user
        if user.is_superuser or user.role in ['super_admin', 'principal', 'vice_principal']:
            return Message.objects.all()
        return Message.objects.filter(models.Q(sender=user) | models.Q(recipient=user))

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class CareerTalkSessionViewSet(viewsets.ModelViewSet):
    queryset = CareerTalkSession.objects.all()
    serializer_class = CareerTalkSessionSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]