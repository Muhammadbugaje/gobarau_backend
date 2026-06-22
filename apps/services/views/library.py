from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.services.models.library import Book, BorrowRecord, LibraryFine
from apps.services.serializers.library import BookSerializer, BorrowRecordSerializer, LibraryFineSerializer
from core.permissions import IsStaffOrAdmin


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]

class LibraryFineViewSet(viewsets.ModelViewSet):
    queryset = LibraryFine.objects.all()
    serializer_class = LibraryFineSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]