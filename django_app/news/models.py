from django.db import models


class Article(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=100, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, null=True)
