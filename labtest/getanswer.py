# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan
@contact:  
@time: 2020/9/23 21:25
@file: getanswer.py
@desc:  
"""

#encoding=utf-8
from gensim.models import word2vec
import sys
sentences=word2vec.Text8Corpus(u'res.txt')
s="hadoop"
print("搜索跟他相关的名词：",s)
model=word2vec.Word2Vec(sentences, size=10)
for i in model.most_similar(s,topn=20):
    print (i[0],i[1])


from jieba import analyse
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags
textrank = analyse.textrank

filename = "res.txt"
# 基于TF-IDF算法进行关键词抽取
content = open(filename, 'rb').read()
keywords = tfidf(content)
print ("keywords by tfidf:")
# 输出抽取出的关键词
for keyword in keywords:
   print (keyword + "\n")


import collections
#coding=utf-8
filename = "res.txt"
with open (filename,'rb') as f:
    words_box=[]
    words_box2=[]
    for line in f:
        line.decode("utf-8")
        words_box.extend(line.strip().split())
    for word in words_box:
        word2 = word.decode("utf-8")
        words_box2.append(word2)
print("词的总数为：%s"%len(words_box2))
print("词频结果：%s"%collections.Counter(words_box2))




# print ("\nkeywords by textrank:")
# # 基于TextRank算法进行关键词抽取
# keywords = textrank(content)
# # 输出抽取出的关键词
# for keyword in keywords:
#     print (keyword)
# print("end")