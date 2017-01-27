from __future__ import unicode_literals

from django.db import models


# Create your models here.
class URLShortenerModel(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=60)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['original_url', 'short_url']

    def __unicode__(self):
        return {0}.format(self.original_url)
