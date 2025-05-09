from django.db import models

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('HR', 'HR'),
        ('Behavioral', 'Behavioral'),
    ]
    
    text = models.CharField(max_length=255,unique=True)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    thought_process= models.TextField()

    def __str__(self):
        return self.text[:50]