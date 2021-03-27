import feedparser


class RSSParser():

    def __init__(self, url, *args, **kwargs):
        super(RSSParser, self).__init__(*args, **kwargs)
        self.url = url
        self.parse = feedparser.parse(self.url)

    def get_source(self):
        feed = self.parse.get('feed')
        return {
            'link': feed.get('link'),
            'title': feed.get('title'),
            'subtitle': feed.get('subtitle'),
        }

    def get_articles(self):
        articles = []
        entries = self.parse.get('entries')
        for entry in entries:
            articles.append({
                'id': entry.get('id'),
                'link': entry.get('link'),
                'title': entry.get('title'),
                'summary': entry.get('summary'),
                'published': entry.get('published_parsed'),
            })

        return articles


if __name__ == '__main__':
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    rss = RSSParser(url)
    print(rss.get_source())
    art = rss.get_articles()
    print(len(art))