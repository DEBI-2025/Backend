from django.contrib import admin
from .models import Field, Level, Topic, Question,Quiz,Choice,UserQuizzesResults

admin.site.register(Field)
admin.site.register(Level)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(UserQuizzesResults)