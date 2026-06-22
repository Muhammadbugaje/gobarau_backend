from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.accounts.models import Person, User
from apps.accounts.serializers import PersonSerializer, UserSerializer
from core.permissions import IsAdminLevel, IsStaffOrAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminLevel]
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated, IsStaffOrAdmin]