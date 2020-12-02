from django.db import models


class Tournament(models.Model):
    name = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now=True)
    participants = models.IntegerField(default=32)
