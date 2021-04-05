import asyncio
import re

from feedparser_data import RssAsync


class RSSParser():

    def __init__(self, url, *args, **kwargs):
        super(RSSParser, self).__init__(*args, **kwargs)
        self.url = url
        self.parse = self.async_parser()

    def get_source(self, feed):
        return {
            'url': self.url,
            'link': self.clean_string('(?<!\/)\/(?!\/)', feed.get('link')),
            'title': feed.get('title'),
            'subtitle': feed.get('subtitle'),
            'updated': feed.get('updated_parsed'),
            'new_entries': 0
        }

    def get_articles(self, entries):
        articles = []
        for entry in entries:
            articles.append({
                'id': entry.get('id'),
                'link': self.clean_string('(?<!\/)\/(?!\/)', entry.get('link')),
                'title': entry.get('title'),
                'summary': self.clean_string('<+', entry.get('summary')),
                'media_content': entry.get('media_content'),
                'published': entry.get('published_parsed'),
            })

        return articles

    async def async_parser(self):
        parse = {}
        rss = RssAsync()
        data = await rss.get_data(url_to_parse=self.url,
                                  bypass_bozo=True)
        parse['source'] = self.get_source(data.feed)
        parse['articles'] = self.get_articles(data.entries)

        return parse

    @staticmethod
    def clean_string(regexp, string):
        return re.split(regexp, string)[0]


if __name__ == '__main__':
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    rss = RSSParser(url)
    # art = rss.articles
    # print(rss.source)
    # print(art)
    asyncio.run(rss.parse)
