#coding=utf-8

import sys

f = open("country_list.txt")
country_list = f.read().split("\n")
f.close()
wiki_data = sys.stdin
for line in wiki_data:
    for country_name in country_list:
        line = line.replace(country_name,country_name.replace(" ","_"))
    print line, #,を入れると改行されない

