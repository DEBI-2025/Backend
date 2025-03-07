from django.db import models

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