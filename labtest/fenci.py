# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan
@contact:  
@time: 2020/9/23 21:14
@file: fenci.py
@desc:  
"""

#encoding=utf-8
#
filename = "stop_words.txt"

f = open(filename,"r",encoding='utf-8')
result = list()
for line in f.readlines():
    line = line.strip()
    if not len(line):
        continue

    result.append(line)
f.close
with open("stop_words2.txt","w",encoding='utf-8') as fw:
    for sentence in result:
        sentence.encode('utf-8')
        data=sentence.strip()
        if len(data)!=0:
            fw.write(data)
            fw.write("\n")
print ("end")
