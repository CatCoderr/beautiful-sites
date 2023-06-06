from rest_framework import serializers
from rest_framework import viewsets
from gallery.models import ArtExhibition


class ArtExhibitionSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(many=True, read_only=True, slug_field='image_url')

    class Meta:
        model = ArtExhibition
        fields = '__all__'


class ArtExhibitionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArtExhibition.objects.all()
    serializer_class = ArtExhibitionSerializer
