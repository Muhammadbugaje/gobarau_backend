from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.content.models import (
    NewsCategory, NewsPost, Event, GalleryAlbum, GalleryImage,
    MagazineIssue, MagazineArticle, YearbookSet, YearbookEntry, Testimonial
)

from apps.content.serializers import (
    NewsCategorySerializer, NewsPostSerializer, EventSerializer, GalleryAlbumSerializer,
    GalleryImageSerializer, MagazineIssueSerializer, MagazineArticleSerializer,
    YearbookSetSerializer, YearbookEntrySerializer, TestimonialSerializer
)

from core.permissions import IsStaffOrAdmin


class ContentPublicReadOnlyModelViewSet(viewsets.ModelViewSet):
    """Base ViewSet allowing public read, but staff-only write."""
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated(), IsStaffOrAdmin()]

class NewsCategoryViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer

class NewsPostViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = NewsPost.objects.all()
    serializer_class = NewsPostSerializer

class EventViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class GalleryAlbumViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = GalleryAlbum.objects.all()
    serializer_class = GalleryAlbumSerializer

class GalleryImageViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class MagazineIssueViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = MagazineIssue.objects.all()
    serializer_class = MagazineIssueSerializer

class MagazineArticleViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = MagazineArticle.objects.all()
    serializer_class = MagazineArticleSerializer

class YearbookSetViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = YearbookSet.objects.all()
    serializer_class = YearbookSetSerializer

class YearbookEntryViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = YearbookEntry.objects.all()
    serializer_class = YearbookEntrySerializer

class TestimonialViewSet(ContentPublicReadOnlyModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer