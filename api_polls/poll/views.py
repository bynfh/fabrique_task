from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll, Question, Vote
from .serializers import PollSerializer, QuestionSerializer, VoteSerializer
from .permissons import PollPermission, QuestionPermission
from .filters import VoteFilter


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (PollPermission, )

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        serializer = SnippetSerializer
        return Response(serializer.data)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend, )
    http_method_names = ('get', 'post')
    filterset_class = VoteFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (QuestionPermission, )


