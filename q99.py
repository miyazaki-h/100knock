#coding=utf-8 

import sys 
from sklearn.externals import joblib
from sklearn.manifold import TSNE #データ可視化のための次元削減
import matplotlib.pyplot as plt #2次元グラフィック表示
import numpy as np


country_word_vec = joblib.load(sys.stdin)
country_names = country_word_vec.keys() #.key():リストのkeyを出力
country_vec = country_word_vec.values() #.value():リストのvalueを抽出

model = TSNE(n_components=2) #データを二次元にまとめる
country_vec_tsne = model.fit_transform(country_vec) #ベクトルのデータを埋め込まれたスペースに入れた形にして返す

plt.scatter(country_vec_tsne[:, 0],country_vec_tsne[:, 1],s = 0.01) #散布するデータを決める。sはプロットのサイズ
plt.title("No.99")
plt.xlabel("x")
plt.ylabel("y")

for countries,vec in zip(country_names,country_vec_tsne):
    plt.annotate(countries, xy  = (vec[0],vec[1]),size=3.) #散布するプロットに名前をつけて、それぞれ出力
plt.savefig("q99.pdf")

