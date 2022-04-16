__author__ = 'Eren Turkay <turkay.eren@gmail.com>'

from datetime import datetime

from scrapy.dupefilters import BaseDupeFilter
import logging
from scrapy.utils.request import request_fingerprint

from .models import Seen, session, create_tables
from .utils import is_request_seen


class DatabaseDupeFilter(BaseDupeFilter):
    def __init__(self):
        create_tables()

    def log(self, *args, **kwargs):
        logging.log(kwargs["level"], args[0])

    def request_seen(self, request):
        is_seen = is_request_seen(request)

        if not is_seen:
            self.log('New URL: %s. Adding it to seen database' % request.url, level=logging.DEBUG)
            seen = Seen(fingerprint=request_fingerprint(request),
                        url=request.url,
                        last_crawl_time=datetime.now())
            try:
                session.add(seen)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()
        else:
            self.log('[seen] "%s" is seen. Skipping.' % request.url, level=logging.INFO)

        return is_seen