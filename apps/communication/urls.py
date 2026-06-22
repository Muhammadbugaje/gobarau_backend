from rest_framework.routers import DefaultRouter
from apps.communication.views import (
    AnnouncementViewSet, NotificationViewSet, MessageViewSet,
    QuestionViewSet, CareerTalkSessionViewSet
)


router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'career-talk-sessions', CareerTalkSessionViewSet, basename='career-talk-session')
urlpatterns = router.urls