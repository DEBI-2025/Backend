from django.db import models
import sys
sys.path.append('../accounts')
from accounts.models import UserAccount

class Field(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=255)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="topics")

    def __str__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="questions")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="questions")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="questions")
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class Quiz(models.Model):
    text = models.TextField(unique=True)
    answer_reason = models.TextField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="quiz")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="quiz")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="quiz")

    def __str__(self):
        return self.text

class Choice(models.Model):
    quiz_question=models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="choices")
    label=models.CharField(max_length=1)
    choice_text = models.TextField()
    is_correct = models.BooleanField(default=False)

class UserQuizzesResults(models.Model):
    user=models.ForeignKey(UserAccount , on_delete=models.CASCADE, related_name="quizzesResults")
    takenQuizzes= models.IntegerField(default=0)
    passedQuizzes= models.IntegerField(default=0)
    highestGrade = models.FloatField(default=0)
    successRate = models.FloatField(default=0)