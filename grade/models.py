from django.db import models


class Grade(models.Model):
    subject = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    full = models.IntegerField(default=0)
