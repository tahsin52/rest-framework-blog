from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):


    " Her türlü çalışır ve girişi kontrol eder girmediysek erişemeyiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    message = "You must be the owner of this object."

    "Sadece delete yapıldıgında çalışır erişebiliriz ancak delete yaptığımızda yetkimizin olmadığını söyler"


    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user) or request.user.is_superuser

