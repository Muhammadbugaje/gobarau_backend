from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.content.models import (
    NewsCategory, NewsPost, Event, GalleryAlbum, GalleryImage,
    MagazineIssue, MagazineArticle, YearbookSet, YearbookEntry, Testimonial
)


@admin.register(NewsCategory)
class NewsCategoryAdmin(ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'description')


@admin.register(NewsPost)
class NewsPostAdmin(ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'is_featured', 'is_published')
    list_filter = ('is_published', 'is_featured', 'category')
    search_fields = ('title', 'body')
    readonly_fields = ('slug', 'created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('title', 'event_date', 'venue', 'is_public')
    list_filter = ('is_public', 'event_date')
    search_fields = ('title', 'description', 'venue')

@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(ModelAdmin):
    list_display = ('title', 'event', 'created_at')
    list_filter = ('event',)
    search_fields = ('title', 'description')

@admin.register(GalleryImage)
class GalleryImageAdmin(ModelAdmin):
    list_display = ('album', 'caption', 'order_index', 'uploaded_by')
    list_filter = ('album',)
    search_fields = ('caption',)

@admin.register(MagazineIssue)
class MagazineIssueAdmin(ModelAdmin):
    list_display = ('title', 'issue_number', 'volume', 'publication_date')
    search_fields = ('title', 'issue_number', 'volume')

@admin.register(MagazineArticle)
class MagazineArticleAdmin(ModelAdmin):
    list_display = ('title', 'issue', 'author_name', 'page_number')
    list_filter = ('issue',)
    search_fields = ('title', 'author_name', 'body')

@admin.register(YearbookSet)
class YearbookSetAdmin(ModelAdmin):
    list_display = ('title', 'session', 'publication_date')
    list_filter = ('session',)
    search_fields = ('title',)

@admin.register(YearbookEntry)
class YearbookEntryAdmin(ModelAdmin):
    list_display = ('yearbook_set', 'student', 'nickname')
    list_filter = ('yearbook_set',)
    search_fields = ('student__user__username', 'nickname', 'quote')

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('person_name', 'role', 'is_featured', 'published_at')
    list_filter = ('is_featured',)
    search_fields = ('person_name', 'role', 'message')