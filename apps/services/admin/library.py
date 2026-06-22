from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.services.models.library import Book, BorrowRecord, LibraryFine


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'quantity_total', 'quantity_available')
    list_filter = ('genre',)
    search_fields = ('title', 'author', 'isbn')

@admin.register(BorrowRecord)
class BorrowRecordAdmin(ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_date', 'due_date', 'return_date', 'status')
    list_filter = ('status', 'borrow_date')
    search_fields = ('book__title', 'borrower__user__username')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(LibraryFine)
class LibraryFineAdmin(ModelAdmin):
    list_display = ('borrow_record', 'amount', 'paid', 'paid_at')
    list_filter = ('paid',)
    search_fields = ('borrow_record__book__title',)