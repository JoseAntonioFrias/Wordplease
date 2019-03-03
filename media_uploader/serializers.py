from rest_framework import serializers
from media_uploader.models import Media


class MediaUploaderSerializer(serializers.ModelSerializer):
    relative_uri = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ['media_name', 'relative_uri']

    def get_relative_uri(self, obj):
        return str(obj.media_name.url)
