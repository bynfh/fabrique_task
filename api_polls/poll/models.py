import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Choice(models.Model):
    question = models.ForeignKey(
        'Question', related_name='choices', on_delete=models.CASCADE
    )
    text = models.CharField(max_length=64, default='Enter value')


class Poll(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField(max_length=1000)


class Question(models.Model):

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

    type = models.CharField(max_length=2, choices=Type.Choices, default=Type.COMMON_TXT)


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=datetime.date.today(), editable=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, related_name='answers', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    value = models.CharField(max_length=128, blank=True, null=True)



