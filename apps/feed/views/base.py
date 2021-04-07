import asyncio
from django.views.generic import DetailView

from apps.feed.models import Feed
from asgiref.sync import sync_to_async 

class BaseDetailView(DetailView):
    async def get_feeds(self):
        # loop = asyncio.get_event_loop()
        async_query = sync_to_async(Feed.objects.filter(user=self.request.user))
        task = [self.feed_attr(feed) for feed in async_query]
        # for i in task:
        #     print("adaedae--->>>  ", type(i))
        corut = await asyncio.gather(*task)
        # results = loop.run_until_complete(corut)
        print("AAAAAAA")
        print(corut)
        return corut

    async def feed_attr(self, feed):
        rss = feed.parse()
        async_resp = await rss.parse
        return {
            'source': async_resp.get('source'),
            'articles': async_resp.get('articles'),
            'pk': feed.id
        }
