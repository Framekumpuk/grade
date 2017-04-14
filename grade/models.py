from django.db import models


class Grade(models.Model):
    subject = models.CharField(max_length=200)
    score = models.FloatField(default=0)
    full = models.FloatField(default=0)
    total = models.FloatField(default=0)
