#coding=utf-8

import sys
from sklearn.externals import joblib
from tqdm import tqdm

country_word_vec = dict()
with open("country_list.txt") as country_list:
    word_dic = joblib.load(sys.stdin)
    word_vectors = joblib.load(sys.argv[1])
    for country in tqdm(country_list):
        country_name = country.strip(".,!?;:\(\)\[\]\'\"").rstrip().replace(" ","_")
        if country_name in word_dic:
            country_word_vec[country_name] = word_vectors[word_dic[country_name]]
    joblib.dump(country_word_vec,"country_word_vec.dump")
