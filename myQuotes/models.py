from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.CharField(max_length=100)