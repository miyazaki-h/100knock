#coding=utf-8

import sys
import numpy as np
from gensim.models import Word2Vec
import cPickle as pickle #いろいろなオブジェクトをバイト化して保存するための関数
from sklearn.externals import joblib #pickleと同じ？
from tqdm import tqdm
model = Word2Vec.load_word2vec_format("w2v.txt", binary = False) 
pickle.dump(model,open("w2v.dump","w")) #データをバイト化して圧縮
model = Word2Vec.load("w2v.dump")

word_dic = dict() #辞書を作る
for index,word in enumerate(model.vocab.keys()): #enumerate:ループの際にindex付きでデータを得る,,model.vocab.keys():登録されている語のリストを取り出す
    word_dic[word] = index
joblib.dump(word_dic,"word_dic.dump")

word_vectors = np.ndarray((len(word_dic),300)) #300次元、要素数がwordの数ある行列
for word,index in tqdm(word_dic.iteritems()): #interitems():idexと要素を同時に取り出せる
    word_vectors[index] = model[word] #model[x]でxについてのベクトルを取得する
joblib.dump(word_vectors,"word_vectors.dump")
