# -*- coding: utf-8 -*-

# Scrapy settings for sozlukcrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# MySQL, PostgreSQL, veya SQLite kullanilabilir. ORM olarak SQLAlchemy kullanildigi
# icin SQLAlchemy'nin destekledigi butun engine ayarlarini kullanabilirsiniz.
#
# Herhangi bir veritabani kurmak, kullanici olusturmak istemiyorsaniz SQLite ile
# tek dosyaya yazabilir ve okuyabilirsiniz. Bunun icin asagidaki satirlarin yorumunu
# kaldirin.
#
# SQLite Ayari
# ============
# DATABASE = {
#     'drivername': 'sqlite',
#     'database': 'db.sqlite'
# }
#
#
# PostgreSQL ve MySQL kullanmak istiyorsaniz ne yaptiginizi bildiginizi varsayarak veritabani ve
# kullanici olusturmayi pas geciyorum.
#
# PostgreSQL
# ==========
DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': 'localhost',
    'port': '5432',
    'username': 'sozlukcrawl',
    'password': 'sozlukcrawl',
    'database': 'sozlukcrawl'
}


# MySQL
# =====
# DATABASE = {
    # 'drivername': 'mysql',
    # 'host': 'localhost',
    # 'port': '3306',
    # 'username': 'sozlukcrawl',
    # 'password': 'sozlukcrawl',
    # 'database': 'sozlukcrawl'
# }

LOG_ENABLED = True
LOG_LEVEL = 'INFO'

BOT_NAME = 'sozlukcrawl'

SPIDER_MODULES = ['sozlukcrawl.spiders']
NEWSPIDER_MODULE = 'sozlukcrawl.spiders'

RETRY_ENABLED = False
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'sozlukcrawl.middleware.RandomUserAgent': 1,
    'sozlukcrawl.middleware.ErrorMonkeyMiddleware': 2,
}

ITEM_PIPELINES = {
    'sozlukcrawl.pipelines.DatabasePipeline': 0,
}

DUPEFILTER_CLASS = 'sozlukcrawl.dupefilter.DatabaseDupeFilter'

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
