from rest_framework.routers import DefaultRouter
from apps.content.views import (
    NewsCategoryViewSet, NewsPostViewSet, EventViewSet, GalleryAlbumViewSet,
    GalleryImageViewSet, MagazineIssueViewSet, MagazineArticleViewSet,
    YearbookSetViewSet, YearbookEntryViewSet, TestimonialViewSet
)


router = DefaultRouter()
router.register(r'news-categories', NewsCategoryViewSet, basename='news-category')
router.register(r'news-posts', NewsPostViewSet, basename='news-post')
router.register(r'events', EventViewSet, basename='event')
router.register(r'gallery-albums', GalleryAlbumViewSet, basename='gallery-album')
router.register(r'gallery-images', GalleryImageViewSet, basename='gallery-image')
router.register(r'magazine-issues', MagazineIssueViewSet, basename='magazine-issue')
router.register(r'magazine-articles', MagazineArticleViewSet, basename='magazine-article')
router.register(r'yearbook-sets', YearbookSetViewSet, basename='yearbook-set')
router.register(r'yearbook-entries', YearbookEntryViewSet, basename='yearbook-entry')
router.register(r'testimonials', TestimonialViewSet, basename='testimonial')
urlpatterns = router.urls