# Sözlük Crawler
Orijinal readme [burada](https://github.com/eren/sozlukcrawler#readme)

## Kurulum:
- Python 3.9 ve pip yukleyin
- `python3 -m venv venv` ve `source venv/bin/activate`
- Postgresql kurulumu, yeni kullanici ve db olusturma (settings.py icine bakin)

## Kullanim
- Crawl: `scrapy crawl eksisozluk -a baslik="https://eksisozluk.com/github--1995063"` (debug seviyei log icin ` -L DEBUG` ekleyin)
- Database verilerini silme (postgresql): `psql -U sozlukcrawl -c 'DELETE FROM seen; DELETE FROM girdiler;'`