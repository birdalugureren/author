from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    tags = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='authors', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Author, self).save(*args, **kwargs)
