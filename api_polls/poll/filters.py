import django_filters

from .models import Vote


class VoteFilter(django_filters.FilterSet):
    """
    Filter vote on fields user and poll

    """

    class Meta:
        model = Vote
        fields = {
            'user': ['exact', 'isnull'],
            'poll': ['exact'],
        }
