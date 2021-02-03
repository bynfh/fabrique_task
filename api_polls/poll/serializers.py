from rest_framework import serializers

from .fields import ObjectIDField
from .models import Poll, Question, Choice, Answer, Vote


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')
        read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=Question.Type.Choices, default=Question.Type.COMMON_TXT
    )
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'question_txt', 'type', 'choices')
        read_only_fields = ('id',)
        extra_kwargs = {
            'poll': {'write_only': True}
        }


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_date', 'finish_date', 'description', 'questions')
        read_only_fields = ('id',)

    def validate_start_date(self, value):
        if self.instance and self.instance.start_date < value:
            raise serializers.ValidationError(
                "After create poll you can't change start date"
            )

        return value


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    choice_id = ObjectIDField(queryset=Choice.objects.all(), write_only=True)
    question = QuestionSerializer(read_only=True)
    question_id = ObjectIDField(queryset=Question.objects.all(), write_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'question', 'choice', 'value')
        read_only_fields = ('id',)


class VoteSerializer(serializers.ModelSerializer):
    poll = PollSerializer(read_only=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Vote
        fields = ('id', 'poll_id', 'poll', 'user', 'date', 'answers')
        read_only_fields = ('id', 'user', 'date')