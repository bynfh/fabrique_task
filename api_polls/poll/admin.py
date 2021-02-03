from django.contrib import admin
from .models import Poll, Question, Answer, Vote


class AdminPoll(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'finish_date', 'description']
    list_editable = ['description']


class AdminQuestion(admin.ModelAdmin):
    list_display = ['type', 'question_txt']
    list_editable = ['question_txt']


admin.site.register(Poll, AdminPoll)
admin.site.register(Question, AdminQuestion)
admin.site.register(Answer)
admin.site.register(Vote)