from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'public_date', 'was_published_recently')
    list_filter = ['public_date']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date infomation', {'fields': ['public_date']}),
        ]
    inlines = [ChoiceInLine]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)