from django.db import models


class Note(models.Model):
    content = models.CharField(max_length=2000)
    created_date = models.DateTimeField()

