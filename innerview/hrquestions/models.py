from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('HR', 'HR'),
        ('Behavioral', 'Behavioral'),
    ]
    
    text = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.text[:50]