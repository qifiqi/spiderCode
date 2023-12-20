# -*- coding: utf-8 -*-
# All Rights Reserved 
# @Time    : 2023/10/2422:18
# @Author  : Small Fu
# @Email   : 2737454073@qq.com
# @File    : topic_3.py
__author__ = 'Small Fu'

import requests

sess = requests.session()

headers = {
    "Host": "match.yuanrenxue.cn",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "Accept": "*/*",
    "Origin": "https://match.yuanrenxue.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://match.yuanrenxue.cn/match/3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "qpfccr=true; no-alert3=true"
}
sess.headers = headers
for i in range(1, 6):
    url = "https://match.yuanrenxue.cn/jssm"
    response = sess.post(url, headers=headers)
    sess.headers['Cookie'] = response.headers['Set-Cookie']

    url = f"https://match.yuanrenxue.cn/api/match/3?page={i}"
    response = sess.get(url, headers=headers)
    print(response.json())
