from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 2

class QuestionAdmin(admin.ModelAdmin):
  fieldsets: [
    (None, {'fields': ['text']}),
    ('Publish date', {'fields': ['publish_date']})
  ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
