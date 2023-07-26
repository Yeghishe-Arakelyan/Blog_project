from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to allow only the owner of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS requests (read-only permissions) for all users.
        if request.method in SAFE_METHODS:
            return True
        
        # Allow PUT, PATCH, and DELETE requests (edit or delete permissions) only for the owner of the object.
        return obj.author == request.user


class CommentDeletePermission(BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
       
        return request.user == obj.author or request.user == obj.post.author
    

class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated and (request.user == view.get_object() or request.user.is_staff)