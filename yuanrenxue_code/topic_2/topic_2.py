# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/10/1121:55
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : topic_2.py
__author__ = 'Small Fu'
import requests
import json,os

headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://match.yuanrenxue.cn/match/2",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
import execjs
code = execjs.compile(open("./topic_2.js",'r',encoding='utf-8').read())
num = 0
for i in range(1,6):
    url = "https://match.yuanrenxue.cn/api/match/2"
    params = {
        "page": i
    }
    headers['Cookie'] = code.call('get_cookies')
    response = requests.get(url, headers=headers, params=params)
    print(response.json())
    num += sum([i['value'] for i in response.json()['data']])
print(num)