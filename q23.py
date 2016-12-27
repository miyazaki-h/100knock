# coding=utf-8                                                                                                                                                                                              
import json
import gzip
import re
country_data = dict()
with gzip.open("jawiki-country.json.gz","rt") as data_file:
    for line in data_file:
        country_data = json.loads(line)
        if country_data["title"] == u"イギリス":
           break

pattern = re.compile(r"==+.+==+")
for line in country_data["text"].split("\n"):
    p = re.search(pattern, line)
    if p:
        level = p.group().rstrip("=").count("=") -1
        print p.group().strip("=") + ":" + str(level)

