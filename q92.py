#coding=utf-8
#コサイン類似度:ベクトルのなす角度の近さ
import sys
import numpy as np #数学関数
from sklearn.externals import joblib
from gensim.models import Word2Vec
from tqdm import tqdm #ループの進捗情報を確認する関数

def cos_sim_max(v,word_dic,word_vectors): #コサイン類似度が最大の単語を求める関数
    word_cos_sim = 0.0
    word_sim_max = ""
    for word,index in word_dic.iteritems(): #iteritems()は辞書からkeyとvalueを取得する
        vector = word_vectors[index]
        cos_sim_temp = np.dot(v,vector)/(np.linalg.norm(v)*np.linalg.norm(vector)) #np.dotは内積を計算、np.linalg.normはノルムを計算
        if word_cos_sim < cos_sim_temp:
            word_cos_sim = cos_sim_temp
            word_sim_max = word
    return word_sim_max, word_cos_sim

def main():
    with open("family.txt") as f:
        word_dic = joblib.load(sys.stdin)
        word_vectors = joblib.load(sys.argv[1])
        for line in tqdm(f):
            if line.startswith(":"):
                continue # :familyの列は除く
            else :
                words = line.rstrip().split( )
                word1 = words[0]
                word2 = words[1]
                word3 = words[2]
                word4 = words[3]
                if (word1 in word_dic) and (word2 in word_dic) and (word3 in word_dic):
                    v1 = word_vectors[word_dic[word1]]
                    v2 = word_vectors[word_dic[word2]]
                    v3 = word_vectors[word_dic[word3]]
                    v = v2 - v1 + v3
                
                    w, sim_cos = cos_sim_max(v,word_dic,word_vectors) 
        
                    print "{} {} {} {} {} {}".format(word1.encode("utf-8"),word2.encode("utf-8"),word3.encode("utf-8"),word4.encode("utf-8"),w.encode("utf-8"),sim_cos)
                else:
                    print "{} {} {} {}".format(word1.encode("utf-8"),word2.encode("utf-8"),word3.encode("utf-8"),word4.encode("utf-8"))

if __name__ == '__main__':
    main()
