# -*- coding: utf-8 -*-

"""have a nice day.

@author: Khan
@contact:  
@time: 2020/9/22 17:21
@file: demo1.py
@desc:  
"""

import json
import random
import traceback
from JobCatch.clear import clear_text
from JobCatch.ciyun import ciyun
import requests
from lxml import etree
import time
from JobCatch.demo2 import getdetail

user_Agent = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0', 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'
]

#代理ip 已经用不了了
# proxy_list=[

# ]

jobs_info=[]
key="java"
url='https://www.liepin.com/zhaopin/'

# try:
#爬了10页
for i in range(10):
    print(i)
    parmas = {
        'key': key,
        'curPage': i
    }
    requests.adapters.DEFAULT_RETRIES = 5
    page_text = requests.get(url=url, headers={"User-Agent": random.choice(user_Agent)}, params=parmas).text

    tree = etree.HTML(page_text)

    job_list = tree.xpath('//div[contains(@class,"sojob-result")]/ul[contains(@class,"sojob-list")]/li')
    print(job_list)
    # 爬取列表
    for job in job_list:
        # print(job)
        job_info = {}
        company = job.xpath('.//div[contains(@class,"company-info nohover")]/p/a/text()')[0]
        # print(company)
        title = job.xpath('.//div[contains(@class,"job-info")]/h3/a/text()')[0]
        title = title.strip()
        href = job.xpath('.//div[contains(@class,"job-info")]/h3/a/@href')[0]
        # print(href)
    # 有些相对链接补齐他的链接
        if href.find("http")==-1:
            href="https://www.liepin.com"+href
        print(href)
        # 爬取详情页函数
        getdetail(href, key)
        require_list = job.xpath('.//div[contains(@class,"job-info")]/p[@class="condition clearfix"]/*/text()')
        place=job.xpath('.//div[contains(@class,"job-info")]/p[@class="condition clearfix"]/a/text()')
        if len(place)==0:
            place=""
        # print(require_list)
        # print(place)
        # print(title)
        # print(href)
        job_info['title'] = title
        job_info['href'] = href
        job_info['company'] = company
        job_info['require_list'] = require_list
        jobs_info.append(job_info)
    time.sleep(3)
    print(jobs_info)

jsonname = key + 'jobs.json'
with open(jsonname, 'w', encoding='utf-8') as file:
    file.write(json.dumps(jobs_info, indent=2, ensure_ascii=False))

# 清洗数据
clear_text(key)

# 分词
ciyun(key)