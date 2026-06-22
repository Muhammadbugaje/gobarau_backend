from django.db import models
from django.utils.text import slugify
from core.models import BaseModel, AuditMixin


class NewsCategory(BaseModel):
    """Category for news posts."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, default="")
    class Meta:
        ordering = ["name"]
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class NewsPost(AuditMixin):
    """School news article."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    body = models.TextField()
    category = models.ForeignKey(
        "content.NewsCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts",
        db_index=True,
    )
    featured_image = models.ImageField(upload_to="content/news/", blank=True, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    is_published = models.BooleanField(default=False, db_index=True)
    class Meta:
        ordering = ["-published_at"]
        verbose_name = "News Post"
        verbose_name_plural = "News Posts"
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Event(BaseModel):
    """School event."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    event_date = models.DateField()
    venue = models.CharField(max_length=200, blank=True, default="")
    cover_image = models.ImageField(upload_to="content/events/", blank=True, null=True)
    is_public = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ["-event_date"]
        verbose_name = "Event"
        verbose_name_plural = "Events"
    def __str__(self):
        return self.title

class GalleryAlbum(BaseModel):
    """Photo album container."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    cover_image = models.ImageField(upload_to="content/gallery/", blank=True, null=True)
    event = models.ForeignKey(
        "content.Event",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="albums",
        db_index=True,
    )
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Gallery Album"
        verbose_name_plural = "Gallery Albums"
    def __str__(self):
        return self.title

class GalleryImage(BaseModel):
    """Individual photo in an album."""
    album = models.ForeignKey(
        "content.GalleryAlbum",
        on_delete=models.CASCADE,
        related_name="images",
        db_index=True,
    )
    image = models.ImageField(upload_to="content/gallery/images/")
    caption = models.CharField(max_length=200, blank=True, default="")
    order_index = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_gallery_images",
        db_index=True,
    )
    class Meta:
        ordering = ["order_index"]
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    def __str__(self):
        return f"Image in {self.album.title}"

class MagazineIssue(BaseModel):
    """School magazine edition."""
    title = models.CharField(max_length=200)
    issue_number = models.CharField(max_length=20)
    volume = models.CharField(max_length=20)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to="content/magazines/", blank=True, null=True)
    pdf_url = models.FileField(upload_to="content/magazines/pdfs/", blank=True, null=True)
    class Meta:
        ordering = ["-publication_date"]
        verbose_name = "Magazine Issue"
        verbose_name_plural = "Magazine Issues"
    def __str__(self):
        return self.title

class MagazineArticle(BaseModel):
    """Article inside a magazine issue."""
    issue = models.ForeignKey(
        "content.MagazineIssue",
        on_delete=models.CASCADE,
        related_name="articles",
        db_index=True,
    )
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200, blank=True, default="")
    body = models.TextField()
    page_number = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["page_number"]
        verbose_name = "Magazine Article"
        verbose_name_plural = "Magazine Articles"
    def __str__(self):
        return self.title

class YearbookSet(BaseModel):
    """Annual yearbook collection."""
    session = models.ForeignKey(
        "administration.AcademicSession",
        on_delete=models.CASCADE,
        related_name="yearbook_sets",
        db_index=True,
    )
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to="content/yearbooks/", blank=True, null=True)
    class Meta:
        ordering = ["-publication_date"]
        verbose_name = "Yearbook Set"
        verbose_name_plural = "Yearbook Sets"
    def __str__(self):
        return self.title

class YearbookEntry(BaseModel):
    """Student entry in a yearbook."""
    yearbook_set = models.ForeignKey(
        "content.YearbookSet",
        on_delete=models.CASCADE,
        related_name="entries",
        db_index=True,
    )
    student = models.ForeignKey(
        "people.StudentProfile",
        on_delete=models.CASCADE,
        related_name="yearbook_entries",
        db_index=True,
    )
    photo = models.ImageField(upload_to="content/yearbooks/students/", blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, default="")
    quote = models.TextField(blank=True, default="")
    future_aspiration = models.TextField(blank=True, default="")
    class Meta:
        ordering = ["student"]
        verbose_name = "Yearbook Entry"
        verbose_name_plural = "Yearbook Entries"
    def __str__(self):
        return f"{self.student} - {self.yearbook_set.title}"

class Testimonial(BaseModel):
    """Alumni or parent testimonial."""
    person_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100, blank=True, default="")
    message = models.TextField()
    photo = models.ImageField(upload_to="content/testimonials/", blank=True, null=True)
    is_featured = models.BooleanField(default=False, db_index=True)
    published_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    def __str__(self):
        return self.person_name