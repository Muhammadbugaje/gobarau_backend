from rest_framework import serializers
from apps.content.models import (
    NewsCategory, NewsPost, Event, GalleryAlbum, GalleryImage,
    MagazineIssue, MagazineArticle, YearbookSet, YearbookEntry, Testimonial
)

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"

class NewsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPost
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class GalleryAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbum
        fields = "__all__"

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = "__all__"

class MagazineIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineIssue
        fields = "__all__"

class MagazineArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineArticle
        fields = "__all__"

class YearbookSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearbookSet
        fields = "__all__"

class YearbookEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = YearbookEntry
        fields = "__all__"

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"