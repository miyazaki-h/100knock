# coding=utf-8

import json,gzip

def uk():
       country_data=dict()
       i = 0
       for country in gzip.open("jawiki-counrty.json.gz"):
              country_data[i]=json.loads(counrty)
              if counrty_data[i]["title"]==u"イギリス":
                     return country_data[i]["text"]
              break
              i+=1

if __name__ == '__main__':
       print uk()


