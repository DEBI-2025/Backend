from django.urls import path
from .views import *

urlpatterns = [
    path('fields/', FieldListView.as_view(), name='fields'),
    path('levels/', LevelListView.as_view(), name='levels'),
    path('topics/', TopicListView.as_view(), name='topics'),
    path('questions/', QuestionListView.as_view(), name='questions'),
    path('quiz/', QuizListView.as_view(), name='quiz'),
    path('getscore/', GetScore.as_view(), name='getscore'),
    path('quizzesResults/', UserQuizzesResultsDetailView.as_view(), name='quizzesResults'), 
]

