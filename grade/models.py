from django.db import models

class Grade(models.Model):
    subject = models.CharField(max_length=200)
    score = models.FloatField(default=0)
    full = models.FloatField(default=0)
    total = models.FloatField(default=0)
    grade = models.CharField(max_length=200)
    credit = models.FloatField(default=0)
    def __str__(self):
        return self.subject
