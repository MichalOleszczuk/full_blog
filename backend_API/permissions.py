from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class YouShallNotPutAndDelete(permissions.BasePermission):
    """
    Custom permission to only allow user to delete or modify itself.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        elif request.method == "POST":
            return True
        elif request.method == "PUT" and obj == request.user:
            return True
        elif request.method == "DELETE" and obj == request.user:
            return True
        else:
            return False