from rest_framework.permissions import  BasePermission


class NotAuthenticated(BasePermission):
    message = "You allready have an account.."
    def has_permission(self, request, view):
        return request.user and not request.user.is_authenticated
