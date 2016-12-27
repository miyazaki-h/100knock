# coding=utf-8
                                                                                                                                                                                              
import json
import gzip
country_data = dict()
with gzip.open("jawiki-country.json.gz","rt") as data_file:
    for line in data_file:
        country_data = json.loads(line)
        if country_data["title"] == u"イギリス":
           break



for line in country_data["text"].split("\n"):
    if "Category" in line:
        print line
