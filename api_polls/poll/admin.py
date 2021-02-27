from django.contrib import admin
from .models import Poll, Question, Answer, Vote


class AdminPoll(admin.ModelAdmin):
    """
    Class for work with Poll model in django admin
    Display from Poll tittle, start_date, finish_date, description
    Edit description from Poll

    """
    list_display = ['title', 'start_date', 'finish_date', 'description']
    list_editable = ['description']


class AdminQuestion(admin.ModelAdmin):
    """
    Class for work with Question model in django admin
    Display from Question type, question_txt
    Edit question_txt from Question

    """
    list_display = ['type', 'question_txt']
    list_editable = ['question_txt']


admin.site.register(Poll, AdminPoll)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer)
admin.site.register(Vote)
