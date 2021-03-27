from apps.feed.rss_parser import RSSParser
from apps.users.models import User
from django.db import models

# Create your models here.

class Feed(models.Model):
    """Model definition for Feed."""

    url = models.URLField(verbose_name="url to suscribe", max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def parse(self):
        return RSSParser(self.url)

    class Meta:
        """Meta definition for Feed."""

        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'

    def __str__(self):
        """Unicode representation of Feed."""
        pass
