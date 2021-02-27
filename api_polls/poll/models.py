from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Poll(models.Model):
    """
    Model for Poll
    :title CharField max_length=200
    :start_date DateField
    :finish_date DateField
    :description TextField max_length=1000

    """
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.title}"


class Question(models.Model):
    """
    Class for model question
    :poll ForeignKey Poll
    :question_txt TextField max_length=2000
    :type CharField max_length=13, choices=Type.Choices, default=Type.COMMON_TXT

    """

    class Type:
        COMMON_TXT = 'Common_txt'
        SINGLE_CHOICE = 'Single_choice'
        MULTI_CHOICE = 'Multi_choice'

        Choices = (
            (MULTI_CHOICE, 'Common_txt'),
            (SINGLE_CHOICE, 'Single_choice'),
            (COMMON_TXT, 'Multi_choice'),
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_txt = models.TextField(max_length=2000)

    type = models.CharField(max_length=13, choices=Type.Choices, default=Type.COMMON_TXT)

    def __str__(self):
        return f"{self.question_txt}"


class Choice(models.Model):
    """
    Class fo model Choice
    :question ForeignKey Question
    :text CharField max_length=64, default='Enter value'

    """
    question = models.ForeignKey(Question, related_name='Choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=64, default='Enter value')

    def __str__(self):
        return f"{self.text}"


class Vote(models.Model):
    """
    Class for model Vote
    :poll ForeignKey Poll
    :user ForeignKey get_user_model()
    :date DateField default=timezone.now() editable=False

    """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now(), editable=False)

    def __str__(self):
        return f"{self.poll}"


class Answer(models.Model):
    """
    Class for model Answer
    :question ForeignKey Question
    :answer_text CharField max_length=100
    :user ForeignKey User

    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer_text}'

    class Meta:
        unique_together = ("question", "user")



