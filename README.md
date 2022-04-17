# Sözlük Crawler
Orijinal readme [burada](https://github.com/eren/sozlukcrawler#readme)

## Kurulum:
- Python 3.9 ve pip yukleyin
- `python3 -m venv venv` ve `source venv/bin/activate`
- Postgresql kurulumu, yeni kullanici ve db olusturma (settings.py icine bakin)

## Kullanim
- Crawl: `scrapy crawl eksisozluk -a baslik="https://eksisozluk.com/sifirdan-tanisilip-sabaha-kadar-konusulan-o-gece--5909637"` (debug seviyei log icin ` -L DEBUG` ekleyin)
- Database verilerini silme (postgresql): `psql -U sozlukcrawl -c 'DELETE FROM seen; DELETE FROM girdiler;'`

## Analiz
- [postgresql sorgular](analysis/sorgular.psql)

| table_name | position | column_name     | data_type                   | max_length | is_nullable | default_value                        |
|------------|----------|-----------------|-----------------------------|------------|-------------|--------------------------------------|
| girdiler   | 1        | id              | integer                     | 32         | NO          | nextval('girdiler_id_seq'::regclass) |
| girdiler   | 2        | source          | character varying           | 20         | YES         | null                                 |
| girdiler   | 3        | girdi_id        | integer                     | 32         | YES         | null                                 |
| girdiler   | 4        | baslik_id       | integer                     | 32         | YES         | null                                 |
| girdiler   | 5        | baslik          | character varying           | 255        | YES         | null                                 |
| girdiler   | 6        | text            | text                        | null       | YES         | null                                 |
| girdiler   | 7        | datetime        | timestamp without time zone | null       | YES         | null                                 |
| girdiler   | 8        | nick            | character varying           | 255        | YES         | null                                 |
| girdiler   | 9        | linkler         | ARRAY                       | null       | YES         | null                                 |
| girdiler   | 10       | favlanma_sayisi | integer                     | 32         | YES         | null                                 |
| seen       | 1        | id              | integer                     | 32         | NO          | nextval('seen_id_seq'::regclass)     |
| seen       | 2        | fingerprint     | character varying           | 40         | YES         | null                                 |
| seen       | 3        | url             | character varying           | 300        | YES         | null                                 |
| seen       | 4        | last_crawl_time | timestamp without time zone | null       | YES         | null                                 |