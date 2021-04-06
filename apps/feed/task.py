import asyncio
from apps.feed.rss_parser import RSSParser
import os
from django.conf import settings
from celery.utils.log import get_task_logger
from celery import shared_task
from celery.decorators import periodic_task

logger = get_task_logger(__name__)


@shared_task
def update_feed(feeds):
    for feed in feeds:
        source = feed.get('source')
        rss = RSSParser(source.get('url'))

        async_resp = asyncio.run(rss.parse)
        check_feed = async_resp.get('source')

        updated = check_feed.get('updated')
        actual = source.get('updated')
        if updated != actual:
            source['new_entries'] += 1

    return feeds
