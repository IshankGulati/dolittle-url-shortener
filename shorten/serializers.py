from rest_framework import serializers
from shorten.models import URLShortenerModel


class URLShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLShortenerModel
        fields = ('original_url', 'short_url')
        read_only_fields = ('id', 'created_at', 'updated_at')
