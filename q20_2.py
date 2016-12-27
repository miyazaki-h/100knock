# coding=utf-8
import json
import gzip
country_data = dict()
with gzip.open("jawiki-country.json.gz","rt") as f:
    for line in f:
        country_data = json.loads(line)
        if country_data["title"] == u"イギリス":
           print country_data["text"]
           break
