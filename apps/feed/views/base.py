import asyncio
from django.views.generic import DetailView

from apps.feed.models import Feed


class BaseDetailView(DetailView):
    def get_feeds(self):
        return [self.feed_attr(feed)
                for feed in Feed.objects.filter(user=self.request.user)]

    def feed_attr(self, feed):
        rss = feed.parse()
        async_resp = asyncio.run(rss.parse)
        return {
            'source': async_resp.get('source'),
            'articles': async_resp.get('articles'),
            'pk': feed.id
        }
