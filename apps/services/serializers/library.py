from rest_framework import serializers
from apps.services.models.library import Book, BorrowRecord, LibraryFine


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = "__all__"

class LibraryFineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryFine
        fields = "__all__"