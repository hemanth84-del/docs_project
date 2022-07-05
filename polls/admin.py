from django.contrib import admin

# Register your models here.
from . models import Question, Choice

# admin.site.register(Question) 
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline): #Tabular/Stacked
    model= Choice
    extra= 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    inlines=[ChoiceInline]
admin.site.register(Question, QuestionAdmin)
