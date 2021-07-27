from django.contrib import admin
from .models import *


# Register your models here.
class TourInline(admin.TabularInline):
    model = Tour
    extra = 0


class QuestionsInline(admin.TabularInline):
    model = Question
    extra = 0


class EventInline(admin.TabularInline):
    model = Event
    extra = 0


class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = (TourInline, EventInline)


class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'quiz', 'num', 'subject')
    inlines = (QuestionsInline, )


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'tour', 'description')


class AnswerTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class CostAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class EventStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'date', 'event_state')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slogan')


# admin.site.register(AnswerType, AnswerTypeAdmin)
# admin.site.register(EventState, EventStateAdmin)
# admin.site.register(Cost, CostAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Event, EventAdmin)
# admin.site.register(Team, TeamAdmin)

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('Title', 'Created_At', 'Updated_At')
#     list_display_links = ('Title', 'Created_At')
#     search_fields = ('Title', 'Content')
#
# admin.site.register(Article, ArticleAdmin)
