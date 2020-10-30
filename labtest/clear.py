# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan
@contact:  
@time: 2020/9/23 21:19
@file: clear.py
@desc:  
"""

#encoding=utf-8
import jieba
from JobCatch.ciyun import ciyun
#数据清洗
def clear_text(key):
    filename = key+"detail.txt"
    stopwords_file = "./stop_words2.txt"

    stop_f = open(stopwords_file,"r",encoding='utf-8')
    stop_words = list()
    wordlist=['熟悉',"任职要求","掌握","负责","精通","工作","岗位","职责",
              "经验","熟练","具备","能力","业务","需求","用户","任职","资格"]

    for line in stop_f.readlines():
        line = line.strip()
        if not len(line):
            continue

        stop_words.append(line)
    stop_f.close

    print(len(stop_words))

    f = open(filename,"r",encoding='utf-8')
    result = list()
    for line in f.readlines():
        line = line.strip()
        # print(line)
        #去掉熟悉无关等词语
        for item in wordlist:
            line=line.replace(item,"")
        # print(line)
        if not len(line):
            continue
        outstr = ''
        seg_list = jieba.cut(line,cut_all=False)
        for word in seg_list:
            if word not in stop_words:
                if word != '\t':
                    outstr += word
                    outstr += " "
       # seg_list = " ".join(seg_list)
        result.append(outstr.strip())
    f.close

    with open(key+"res.txt","w",encoding='utf-8') as fw:
        for sentence in result:
            sentence.encode('utf-8')
            data=sentence.strip()
            if len(data)!=0:
                fw.write(data)
                fw.write("\n")


    print ("end")


if __name__=="__main__":
    # for item in ['java','数据挖掘','图像算法工程师','互联网产品经理']:
    #     # print(item)
    #     clear_text(item)
    #     ciyun(item)
    clear_text("")
    ciyun("")