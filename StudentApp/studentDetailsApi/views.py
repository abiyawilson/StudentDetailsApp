from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from studentDetailsApi.models import StudentTShirtDetails
from studentDetailsApi.serializers import StudentTShirtDetailsSerializers


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user


class StudentRecordViewSet(viewsets.ModelViewSet):
    queryset = StudentTShirtDetails.objects.all()
    serializer_class = StudentTShirtDetailsSerializers
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
