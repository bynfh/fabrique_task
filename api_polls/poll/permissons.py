import datetime
from rest_framework.permissions import SAFE_METHODS, BasePermission


class PollPermission(BasePermission):
    """
    Class for permissions in Poll
    Check permissions for Poll

    """
    def has_permission(self, request, view):
        """
        Common permission for user
        :return True if super user or it is Safe method

        """
        if request.user.is_superuser:
            return True
        view.queryset = view.queryset.filter(finish_date__gte=datetime.date.today())
        if request.method.upper() in SAFE_METHODS:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Check permission for object

        """
        return self.has_permission(request, view)


class QuestionPermission(BasePermission):
    """
    Class for permissions in Question
    Check permissions for Question

    """
    def has_permission(self, request, view):
        """
        Check permissions.
        Only super user received True
        :return bool True or False
        """
        if request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Check permission for object

        """
        return self.has_permission(request, view)
