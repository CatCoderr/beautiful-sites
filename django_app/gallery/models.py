from django.db import models


class ArtExhibition(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    description = models.TextField()
    source = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ArtExhibitionImage(models.Model):
    art_exhibition = models.ForeignKey(ArtExhibition, on_delete=models.CASCADE, related_name='images')
    image_url = models.CharField(max_length=500, null=True)