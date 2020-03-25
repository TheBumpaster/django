from django.contrib.auth.models import User, Group, Permission
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest.serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserModelViewSet(ModelViewSet):
    """
    API Endpoint that allows users to be managed
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupModelViewSet(ModelViewSet):
    """
    API Endpoint that allows groups to be managed
    """
    queryset = Group.objects.all().order_by('-id')
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class PermissionModelViewSet(ModelViewSet):
    """
    API Endpoint that allows groups to be managed
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]