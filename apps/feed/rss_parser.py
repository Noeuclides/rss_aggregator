import feedparser
import re


class RSSParser():

    def __init__(self, url, *args, **kwargs):
        super(RSSParser, self).__init__(*args, **kwargs)
        self.url = url
        self.parse = feedparser.parse(self.url)

    @property
    def source(self):
        feed = self.parse.get('feed')
        return {
            'link': self.clean_string('(?<!\/)\/(?!\/)', feed.get('link')),
            'title': feed.get('title'),
            'subtitle': feed.get('subtitle'),
        }

    @property
    def articles(self):
        articles = []
        entries = self.parse.get('entries')
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

    @staticmethod
    def clean_string(regexp, string):
        return re.split(regexp, string)[0]


if __name__ == '__main__':
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    rss = RSSParser(url)
    art = rss.get_articles()