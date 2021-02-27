from django.conf.urls import url
from django.urls import include
from .views import PollViewSet, QuestionViewSet, VoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)
router.register('votes', VoteViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
