from rest_framework.permissions import BasePermission


class IsAdminForReadOnly(BasePermission):
    """
    Allows public users to create queries.
    Only admin/staff users can read existing queries.
    """

    def has_permission(self, request, view):
        if request.method == "POST":
            return True

        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )