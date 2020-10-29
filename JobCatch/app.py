#1.导入flask扩展
from flask import Flask, request, Response

#2.创建flask应用实例
#需要传入__name__,作用是为了确定资源所在的路径
app = Flask(__name__)

#3.义路由和视图函数

#4.启动程序

import random
import requests
from lxml import etree
import json

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

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/orders/<order_id>')
def get_order_id(order_id):
    return 'order_id %s' % order_id




@app.route('/Getjob')
def Getjob():
    curPage = request.args['curPage']
    key= request.args['key']
    city=request.args['city']
    salary=request.args['salary']
    jobs_info = []
    url = 'https://www.liepin.com/zhaopin/'

    # try:
    # for i in range(10):
    # print(i)
    parmas = {
        'key': key,
        'curPage': curPage,
        'dqs':city,
        'salary': salary
    }
    requests.adapters.DEFAULT_RETRIES = 5
    page_text = requests.get(url=url, headers={"User-Agent": random.choice(user_Agent)}, params=parmas).text

    tree = etree.HTML(page_text)
    # print(tree.text)
    # pageSize=tree.xpath('//div[contains(@class,"container sojob-search")/form/input[@name="d_pageSize"]/@value')[0]
    # print(pageSize)

    job_list = tree.xpath('//div[contains(@class,"sojob-result")]/ul[contains(@class,"sojob-list")]/li')
    print(job_list)
    for job in job_list:
        # print(job)
        job_info = {}
        company = job.xpath('.//div[contains(@class,"company-info nohover")]/p/a/text()')[0]
        # print(company)
        title = job.xpath('.//div[contains(@class,"job-info")]/h3/a/text()')[0]
        title = title.strip()
        href = job.xpath('.//div[contains(@class,"job-info")]/h3/a/@href')[0]
        # print(href)
        if href.find("http") == -1:
            href = "https://www.liepin.com" + href
        print(href)
        require_list = job.xpath('.//div[contains(@class,"job-info")]/p[@class="condition clearfix"]/*/text()')
        place = job.xpath('.//div[contains(@class,"job-info")]/p[@class="condition clearfix"]/a/text()')
        if len(place) == 0:
            place = ""
        # print(require_list)
        # print(place)
        # print(title)
        # print(href)
        job_info['title'] = title
        job_info['href'] = href
        job_info['company'] = company
        job_info['require_list'] = require_list
        jobs_info.append(job_info)
    print(jobs_info)
    return Response(json.dumps(jobs_info, indent=2, ensure_ascii=False),content_type='application/json')



if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
