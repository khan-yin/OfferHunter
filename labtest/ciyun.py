# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan
@contact:  
@time: 2020/10/27 19:00
@file: ciyun.py
@desc:  
"""

#coding:utf-8
import os
import jieba
import wordcloud
import chardet
import imageio
def ciyun(key):

    w=wordcloud.WordCloud(width=1000,height=700,background_color='white',font_path='msyh.ttc',
                          scale=15)
    f = open(key+'res.txt', encoding='utf-8')
    wordlist=f.read()
    txtlist=jieba.lcut(wordlist)
    string="".join(txtlist)


    w.generate(string)
    if key=="":
        key="demo"
    w.to_file(key+'.png')

